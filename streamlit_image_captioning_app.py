
import streamlit as st
import requests
from PIL import Image
from transformers import pipeline
import torch

# Configure Streamlit page
st.set_page_config(
    page_title="Image Captioning",
    page_icon="🖼️",
    layout="wide"
)

# Enhanced CSS for beautiful UI
st.markdown("""
<style>
    .stApp > header {
        background-color: transparent;
    }
    .block-container {
        padding-top: 1rem;
    }
    
    /* Main container styling */
    .main-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    /* Header styling */
    .app-header {
        text-align: center;
        color: white;
        margin-bottom: 2rem;
    }
    
    .app-title {
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .app-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
    }
    
    /* Upload section */
    .upload-container {
        background: rgba(255,255,255,0.95);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    
    /* Caption section */
    .caption-container {
        background: rgba(255,255,255,0.95);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    
    /* Caption display */
    .caption-display {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        font-size: 1.1rem;
        font-style: italic;
        margin: 1rem 0;
        box-shadow: 0 3px 10px rgba(0,0,0,0.2);
        animation: fadeIn 0.5s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    
    /* Stats section */
    .stats-container {
        background: rgba(255,255,255,0.9);
        padding: 1.5rem;
        border-radius: 15px;
        margin-top: 1rem;
        text-align: center;
    }
    
    .stat-item {
        display: inline-block;
        margin: 0 1rem;
        padding: 0.5rem 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 20px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_caption_model():
    """Load the BLIP image captioning model with caching for performance"""
    try:
        # Use CPU by default, GPU if available
        device = 0 if torch.cuda.is_available() else -1
        captioner = pipeline(
            "image-to-text", 
            model="Salesforce/blip-image-captioning-base",
            device=device
        )
        return captioner
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

def generate_caption(image, captioner):
    """Generate caption for the uploaded image"""
    try:
        # Generate more descriptive caption with longer length
        result = captioner(
            image,
            generate_kwargs={
                "max_length": 100,  # Longer for more detail
                "num_beams": 5,     # More beams for better quality
                "do_sample": True,
                "temperature": 0.8, # Slightly more randomness
                "top_p": 0.95,
                "repetition_penalty": 1.1,
                "early_stopping": True
            }
        )
        caption = result[0]['generated_text']
        return caption
    except Exception as e:
        st.error(f"Error generating caption: {e}")
        return None

def main():
    # Initialize session state for caption history
    if 'caption_history' not in st.session_state:
        st.session_state.caption_history = []
    if 'caption_count' not in st.session_state:
        st.session_state.caption_count = 0

    # Beautiful header
    st.markdown("""
    <div class="main-container">
        <div class="app-header">
            <div class="app-title">🖼️ AI Image Captioning</div>
            <div class="app-subtitle">Transform your images into beautiful descriptions</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Load the model
    with st.spinner("🚀 Loading AI model..."):
        captioner = load_caption_model()

    if captioner is None:
        st.error("❌ Failed to load the model. Please refresh the page.")
        return

    # Create two columns for better layout
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<div class="upload-container">', unsafe_allow_html=True)
        st.subheader("📤 Upload Your Image")
        
        # File uploader widget
        uploaded_file = st.file_uploader(
            "Choose an image file",
            type=['jpg', 'jpeg', 'png'],
            help="Supported formats: JPG, JPEG, PNG"
        )

        # Display uploaded image with fixed size
        if uploaded_file is not None:
            try:
                # Load the image
                image = Image.open(uploaded_file)

                # Convert to RGB if necessary
                if image.mode != 'RGB':
                    image = image.convert('RGB')

                # Display image with fixed container size
                st.image(image, caption="📷 Your Image", width=400)
                
                # Image info
                st.success(f"✅ Image loaded: {uploaded_file.name}")

            except Exception as e:
                st.error(f"❌ Error loading image: {e}")
                return
        else:
            st.info("👆 Upload an image to get started")
        
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="caption-container">', unsafe_allow_html=True)
        st.subheader("🤖 AI Generated Caption")
        
        if uploaded_file is not None:
            # Generate Caption button
            if st.button("✨ Generate Caption", type="primary", use_container_width=True):
                with st.spinner("🔄 AI is analyzing your image..."):
                    # Generate caption
                    caption = generate_caption(image, captioner)

                    if caption:
                        # Store in history
                        st.session_state.caption_history.append(caption)
                        st.session_state.caption_count += 1
                        
                        # Display the generated caption with beautiful styling
                        st.markdown(f'<div class="caption-display">"{caption}"</div>', unsafe_allow_html=True)
                        
                        # Show success message
                        st.success("🎉 Caption generated successfully!")

            # Show caption history if available
            if st.session_state.caption_history:
                st.subheader("📝 Caption History")
                for i, hist_caption in enumerate(reversed(st.session_state.caption_history[-3:]), 1):
                    st.markdown(f"**{i}.** {hist_caption}")
                
                # Clear history button
                if st.button("🗑️ Clear History", use_container_width=True):
                    st.session_state.caption_history = []
                    st.session_state.caption_count = 0
                    st.rerun()
        else:
            st.info("👆 Upload an image first to generate captions")
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Stats section
    if st.session_state.caption_count > 0:
        st.markdown("""
        <div class="stats-container">
            <div class="stat-item">📊 Captions Generated: {}</div>
            <div class="stat-item">🎯 Model: BLIP</div>
            <div class="stat-item">⚡ Status: Ready</div>
        </div>
        """.format(st.session_state.caption_count), unsafe_allow_html=True)

if __name__ == "__main__":
    main()