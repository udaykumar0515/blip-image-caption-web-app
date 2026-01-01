# 🖼️ AI Image Captioning Web App

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0%2B-FF4B4B.svg)](https://streamlit.io/)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.12.0%2B-EE4C2C.svg)](https://pytorch.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An intelligent web application that generates descriptive captions for images using state-of-the-art Deep Learning. Built with **Streamlit** and powered by Salesforce's **BLIP** (Bootstrapping Language-Image Pre-training) model.

![App Preview](https://via.placeholder.com/800x400/667eea/ffffff?text=AI+Image+Captioning+App)

## ✨ Features

- 🚀 **Real-time Image Captioning** - Upload images and get AI-generated descriptions instantly
- 🎨 **Beautiful Modern UI** - Gradient-based design with smooth animations and responsive layout
- 📝 **Caption History** - Track and review previously generated captions
- 🔄 **Multiple Format Support** - Works with JPG, JPEG, and PNG images
- ⚡ **GPU Acceleration** - Automatic GPU detection for faster processing
- 🎯 **Advanced Caption Generation** - Fine-tuned parameters for detailed and accurate descriptions

## 🛠️ Technology Stack

- **Frontend**: Streamlit with custom CSS styling
- **AI Model**: [Salesforce BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base) (blip-image-captioning-base)
- **Deep Learning Framework**: PyTorch
- **Transformers**: HuggingFace Transformers library
- **Image Processing**: PIL/Pillow

## 📋 Requirements

- Python 3.8 or higher
- 4GB RAM minimum (8GB recommended)
- GPU support optional (CUDA-compatible GPU for faster inference)

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/udaykumar0515/blip-image-caption-web-app.git
cd blip-image-caption-web-app
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Note**: First run will download the BLIP model (~1GB). Ensure you have a stable internet connection.

## 🎯 Usage

### Running the Application

```bash
streamlit run streamlit_image_captioning_app.py
```

The app will automatically open in your default browser at `http://localhost:8501`

### Using the App

1. **Upload an Image**: Click on "Browse files" and select an image (JPG, JPEG, or PNG)
2. **Generate Caption**: Click the "✨ Generate Caption" button
3. **View Results**: The AI-generated caption will appear with beautiful styling
4. **Caption History**: View your last 3 generated captions
5. **Clear History**: Reset caption history with the clear button

## 📸 Use Cases

- 🦯 **Accessibility** - Generate alt-text for visually impaired users
- 📱 **Social Media** - Auto-generate engaging captions for posts
- 🗂️ **Image Indexing** - Automatically categorize and tag large image databases
- 🛍️ **E-commerce** - Create product descriptions from images
- 📚 **Digital Asset Management** - Organize and search image libraries efficiently

## 🧠 How It Works

The application uses the **BLIP (Bootstrapping Language-Image Pre-training)** model, a state-of-the-art vision-language model developed by Salesforce Research.

### Model Pipeline

1. **Image Upload** → User uploads an image through Streamlit interface
2. **Preprocessing** → Image is converted to RGB and prepared for the model
3. **Feature Extraction** → BLIP's vision encoder extracts visual features
4. **Caption Generation** → Language decoder generates descriptive text using beam search
5. **Display** → Caption is displayed with rich formatting

### Generation Parameters

- **Max Length**: 100 tokens for detailed descriptions
- **Beam Search**: 5 beams for higher quality outputs
- **Temperature**: 0.8 for balanced creativity
- **Top-p Sampling**: 0.95 for diverse yet coherent results
- **Repetition Penalty**: 1.1 to avoid redundant phrases

## 📁 Project Structure

```
blip-image-caption-web-app/
│
├── streamlit_image_captioning_app.py    # Main application file
├── requirements.txt                      # Python dependencies
├── .gitignore                           # Git ignore rules
├── README.md                            # Project documentation
│
├── DL_Course_End_Project_Report.pdf     # Project report (main)
├── DL_Course_End_Project_Report_main.pdf
└── DL_Course_End_Project_Report_starting.pdf
```

## ⚙️ Configuration

The app automatically detects and uses GPU if available. To force CPU usage, modify the model loading section:

```python
device = -1  # Force CPU
```

For custom caption generation settings, adjust parameters in the `generate_caption()` function.

## 🎓 Course Project

This project was developed as a **Deep Learning Course-End Project**, demonstrating:

- Practical implementation of transformer-based vision-language models
- Integration of pre-trained models using HuggingFace
- Building production-ready ML applications with Streamlit
- Understanding of image-to-text generation pipelines
- Modern web UI/UX design principles

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Salesforce Research](https://github.com/salesforce/BLIP) for the BLIP model
- [HuggingFace](https://huggingface.co/) for the Transformers library
- [Streamlit](https://streamlit.io/) for the amazing web framework

## 📧 Contact

**Uday Kumar**

- GitHub: [@udaykumar0515](https://github.com/udaykumar0515)

## 🔗 References

- [BLIP Paper](https://arxiv.org/abs/2201.12086) - Li et al., 2022
- [HuggingFace Model Card](https://huggingface.co/Salesforce/blip-image-captioning-base)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

⭐ **If you found this project helpful, please give it a star!** ⭐
