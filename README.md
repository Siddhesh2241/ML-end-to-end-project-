# End to End Machine learning Project

## 🎓 Student Exam Performance Prediction 📊

Predicting student performance based on demographic and preparatory factors using a machine learning model.

**🌟 Project Overview**

This project is a full End-to-End Machine Learning Web Application that predicts a student's math exam score based on inputs like gender, parental education, test preparation, and more. The application provides a seamless interface for users to enter information and receive predictions for academic performance in real-time.

**🗂️ Project Structure**
```bash
project_root/
├── set.py                     # Information about other and project libraries
├── app.py                     # Main Flask application
├── requirements.txt           # Dependencies
├── Dockerfile                 # Docker setup for the app
├── src/                       # Core code folder
│   ├── components/            # Data ingestion, transformation, and training
│   ├── pipeline/              # Prediction and training pipelines
│   ├── utils.py               # Utility functions
│   ├── logger.py              # Logging configuration
│   └── exception.py           # Exception handling
├── templates/                 # HTML templates
│   ├── index.html             
│   └── home.html
└── static/                    # Static files (CSS, JS)
    └── css/
        └── styles.css         # Styling for the app
```

**🚀 Features**

* Real-Time Predictions: Input student details to instantly predict their math score.
* Customizable: Easily expandable with additional input features or model enhancements.
* Model Training: Full pipeline for model training, evaluation, and hyperparameter tuning.

**🛠️ Technologies Used**
* Frontend: HTML, CSS (optionally with Tailwind CSS)
* Backend: Flask, Python
* Machine Learning Models:
* Random Forest, Decision Tree, Gradient Boosting, XGBoost, CatBoost, and AdaBoost
