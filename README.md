# Falcon9_Prediction

Predict the success of SpaceX Falcon 9 first-stage landings using machine learning and data science approaches.

## Project Overview

This project utilizes publicly available SpaceX API and Wikipedia mission data to build machine learning models that predict Falcon 9 rocket landing outcomes. The goal is to assist launch cost estimation and mission planning based on data-driven insights.

## Features

- Data Collection: Automated via SpaceX REST API and Wikipedia web scraping.
- Data Wrangling & Cleaning: Merges, cleanses, and prepares raw data for modeling.
- Exploratory Data Analysis: Visualizes launch outcomes, examines correlations, and produces statistical summaries.
- Machine Learning Modeling: Trains and validates models (Logistic Regression, SVM, Decision Tree, KNN) to predict landing outcomes.
- Interactive Visualization: Folium maps and dashboards with Plotly Dash for exploring launch site and payload trends.

## Technologies Used

- Python
- Pandas, Numpy
- Scikit-learn
- Matplotlib, Seaborn
- Plotly Dash
- Folium
- BeautifulSoup, Requests
- SQL (optional)

## Project Structure
Falcon9_Prediction/
│
├── data/ # Raw and processed datasets
├── notebooks/ # Jupyter Notebooks for analysis & modeling
├── app.py # Dashboard/web application
├── src/ # Source code for data processing/modeling
├── images/ # Visualizations and results
├── README.md # Project documentation

## Installation & Usage

1. **Clone this repository:**
    ```
    git clone https://github.com/priyanshiiitr/Falcon9_Prediction.git
    cd Falcon9_Prediction
    ```

2. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

3. **Run analysis or dashboard:**
    - Launch dashboard:
        ```
        python app.py
        ```
    - Use Jupyter notebooks:
        ```
        jupyter notebook
        ```

## Example Results

- SVM model achieves over 80% prediction accuracy for Falcon 9 landings.
- Folium maps reveal launch site performance by geography.
- Interactive dashboard supports filtering by payload, site, and orbit features.

## Notebooks

- Data gathering and preprocessing.
- SQL-based exploratory data analysis (optional).
- Feature engineering and visualization.
- Model training and evaluation.

## Contributing

Pull requests are welcome. For major changes, open an issue first to discuss proposed modifications.

## License

MIT License


