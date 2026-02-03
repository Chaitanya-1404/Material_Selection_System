# Material_Selection_System
# ⚙️ Intelligent Material Selection AI 
### *A Machine Learning Approach to Mechanical Engineering Design*

This project implements a **K-Nearest Neighbors (KNN)** algorithm to automate the material selection process in mechanical engineering. By treating material properties as dimensions in a mathematical space, the tool suggests the best candidates based on user-defined design constraints.

---

## 🚀 Project Overview
In mechanical design, selecting a material involves balancing conflicting requirements like high strength vs. low weight. This tool replaces manual datasheet searching with a data-driven approach:
- **Input:** Target values for Strength ($S_u$, $S_y$), Stiffness ($E$), and Density ($R_o$).
- **Logic:** The model calculates the "Euclidean Distance" between your requirements and 1,500+ materials.
- **Output:** Top 5 materials that physically match your design criteria.

## 📁 Repository Structure
* `data/material.csv`: The database containing 1,552 unique material grades and properties.
* `notebooks/project_material.ipynb`: Complete Jupyter Notebook with Exploratory Data Analysis (EDA) and Model Training.
* `app.py`: Streamlit source code for the web-based user interface.
* `material_model.pkl`: The serialized (saved) trained model and scaler.
* `requirements.txt`: List of Python dependencies for easy installation.

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** - `Pandas` & `NumPy` (Data Manipulation)
  - `Scikit-Learn` (Machine Learning & Preprocessing)
  - `Matplotlib` & `Seaborn` (Engineering Visualizations)
  - `Streamlit` (Web Deployment)

## 📊 Key Engineering Visualizations
The project includes several analytical plots crucial for a Mechanical Engineering portfolio:
1. **Correlation Heatmaps:** Verifying physical consistency (e.g., the relationship between Yield and Ultimate strength).
2. **Ashby-style Plots:** Scatter plots of Strength vs. Density to visualize the "Design Space."
3. **Property Distributions:** Understanding the spread of Stiffness ($E$) and Density ($R_o$) across different material families.

## ⚙️ Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Material-Selection-ML.git](https://github.com/YOUR_USERNAME/Material-Selection-ML.git)
   cd Material-Selection-ML
