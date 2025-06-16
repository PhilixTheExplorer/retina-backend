# Retina Backend API

This is a FastAPI backend for retina image analysis using a machine learning model.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Running Locally

### 1. Clone and Navigate to Backend

```bash
cd retina-backend
```

### 2. Create Virtual Environment (Recommended)

But You can skip tho.

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Server

```bash
# For local development
uvicorn main:app --reload

# For external access (accessible from other devices on network)
uvicorn main:app --host=0.0.0.0 --port=8000

# For development with reload and external access
uvicorn main:app --reload --host=0.0.0.0 --port=8000
```

The server will start at:

- Local only: `http://localhost:8000`
- External access: `http://0.0.0.0:8000` (accessible from network devices)
- 0.0.0.0 must be replaced with actual ip address of your computer, when accessed from external device

### 5. Test the Server

Visit `http://localhost:8000` in your browser to see the "Hello Server!" message.

### 6. Test the Prediction API

From Command Prompt or Terminal, You can test the prediction endpoint using curl:

```bash
# Test with a sample image
curl -X POST -F "file=@cat.jpg" https://retina-backend-production.up.railway.app/predict
```

## API Endpoints

- `GET /` - Health check endpoint
- `POST /predict` - Upload image for prediction

## Deployment

requirements.txt and Procfile are for railway config, not related with the model. But you may add extra in requirements.txt according to your needs in the model.

You can just go to your backend api to see server is running. Test with new url if you deploy your own backend server on railway (https://railway.com). This is my test deployment server in railway.

```bash
https://retina-backend-production.up.railway.app/
```
