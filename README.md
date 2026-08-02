# Skin Lesion Classification using Classical Machine Learning

This project explores the classification of skin lesions using handcrafted image features and classical machine learning algorithms on the DermaMNIST dataset.

The objective is to investigate how well traditional computer vision techniques perform compared to modern deep learning approaches for skin lesion classification.

---

## Dataset

This project uses the **DermaMNIST** dataset from the MedMNIST collection.

- Dataset: DermaMNIST
- Number of classes: 7
- Total images: 10,015
- Image size: 28 × 28 RGB
- Task: Multi-class skin lesion classification

Classes:

- Actinic keratoses and intraepithelial carcinoma
- Basal cell carcinoma
- Benign keratosis-like lesions
- Dermatofibroma
- Melanoma
- Melanocytic nevi
- Vascular lesions

---

## Project Structure

```
skin-lesion-classification/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_dataset_exploration.ipynb
│   ├── 02_feature_extraction.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_model_evaluation.ipynb
│
├── results/
│   ├── figures/
│   └── models/
│
├── src/
│
├── requirements.txt
└── README.md
```

---

## Project Progress

### Completed

- ✔ Project setup
- ✔ Dataset download
- ✔ Exploratory Data Analysis (EDA)
  - Dataset overview
  - Sample image visualization
  - Class distribution
  - Pixel intensity statistics

### In Progress

- Handcrafted feature extraction

### Planned

- Histogram of Oriented Gradients (HOG)
- Local Binary Patterns (LBP)
- Color histogram features
- Feature preprocessing
- Model training
- Model comparison
- Performance evaluation
- Model interpretation

---

## Methods

The project focuses on classical computer vision and machine learning techniques.

### Feature Extraction

- Histogram of Oriented Gradients (HOG)
- Local Binary Patterns (LBP)
- Color Histograms

### Machine Learning Models

- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest
- XGBoost

---

## Current Results

Exploratory Data Analysis has been completed.

Feature extraction and model training are currently under development.

---

## Installation

```bash
git clone https://github.com/your-username/skin-lesion-classification.git

cd skin-lesion-classification

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

---

## License

This project is licensed under the MIT License.
