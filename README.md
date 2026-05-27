# Trash Detection System

A web application for real-time trash classification using deep learning. Upload an image and get instant predictions on trash categories.

## 📹 Project Demo

<video width="100%" controls>
  <source src="./project_video.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## 🎯 Overview

This project implements a FastAPI backend with a web frontend for trash classification. The system uses deep learning models to classify waste items into various categories to support recycling and waste management efforts.

## 🏗️ Architecture

```
trash-detection/
├── backend/              # FastAPI backend server
│   ├── main.py          # Main application file
│   ├── config.py        # Configuration settings
│   └── src/             # Source code modules
│       └── utils/       # Utility functions
│           └── prediction.py
├── frontend/            # Web interface
│   └── index.html       # Main HTML file
├── Datasets/            # Training datasets
├── requirements.txt     # Python dependencies
└── project_video.mp4    # Project demonstration video
```

## 🔧 Requirements

- Docker & Docker Compose
- Python 3.8+ (for local development)
- GPU support (optional, for faster inference)

## 📦 Dependencies

- **FastAPI** (0.115.6) - Web framework
- **Uvicorn** (0.34.0) - ASGI server
- **TensorFlow** (2.17.0) - Deep learning
- **PyTorch** (2.0.1) - Deep learning alternative
- **Pillow** (11.1.0) - Image processing
- **Python-multipart** (0.0.20) - File upload handling
- **CORS Middleware** - Cross-origin requests support

## 🐳 Docker Setup

### Building the Docker Image

```bash
docker build -t trash-detection .
```

### Running with Docker

```bash
docker run -p 8000:8000 trash-detection
```

Access the application at: `http://localhost:8000`

### Using Docker Compose

Create a `docker-compose.yml` file:

```yaml
version: '3.8'

services:
  backend:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./:/app
    environment:
      - PYTHONUNBUFFERED=1
    command: uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

Run with Docker Compose:

```bash
docker-compose up
```

## 📝 Dockerfile

Here's the recommended Dockerfile for this project:

```dockerfile
# Use official Python runtime as base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone <https://github.com/seifnasser879/Trash-Detector.git>
   cd trash-detection
   ```

2. **Create virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the backend**
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

5. **Access the application**
   - Open browser and go to `http://localhost:8000`

### Docker Development

1. **Build and run**
   ```bash
   docker build -t trash-detection .
   docker run -p 8000:8000 trash-detection
   ```

2. **Access the application**
   - Open browser and go to `http://localhost:8000`

## 🎨 Frontend Features

- Drag-and-drop image upload
- Real-time classification results
- Support for multiple image formats (PNG, JPG, JPEG, WebP, BMP)
- Responsive web design

## 🤖 API Endpoints

### GET `/`
Returns the frontend HTML interface.

### POST `/classify`
Classifies an uploaded image.

**Request:**
- Content-Type: multipart/form-data
- File: Image file (max 10MB)

**Response:**
```json
{
  "prediction": "plastic"
}
```

**Supported Formats:** PNG, JPG, JPEG, WebP, BMP  
**Max File Size:** 10 MB

**Error Responses:**
- `400` - Invalid file format or size exceeded
- `500` - Prediction error

## 🔒 Security Features

- CORS middleware for controlled cross-origin requests
- File size validation (10MB limit)
- Image format validation
- File type verification

## 📊 Configuration

Edit `backend/config.py` to customize:
- Frontend path
- Model parameters
- Classification thresholds
- API settings

## 🐛 Troubleshooting

### Docker build fails
```bash
# Clear Docker cache and rebuild
docker system prune
docker build --no-cache -t trash-detection .
```

### Port already in use
```bash
# Use a different port
docker run -p 8001:8000 trash-detection
```

### GPU Support (Optional)

For GPU acceleration with Docker:

```bash
docker run --gpus all -p 8000:8000 trash-detection
```

Requires NVIDIA Docker support installed.

## 📈 Performance

- Inference time: < 1 second (CPU)
- < 100ms (GPU)
- Max concurrent requests: Limited by available memory
- Recommended: 4GB+ RAM, GPU optional but recommended

## 📄 License

See LICENSE file for details.

**Happy trash classifying!** ♻️
