
# 🏠 House Price Prediction –AI/ML Internship Task# 06

## 🎯 Objective

This project is part of my AI/ML internship at **DevelopersHub Corporation**. The goal of this project is to predict house prices using machine learning models based on historical housing data from King County, USA. The predictions are based on features like the number of bedrooms, square footage, location, and more.

---

## 📊 Dataset Used

- **Name:** King County House Sales Dataset  
- **Source:** [Kaggle](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction)  
- **File Name:** `kc_house_data.csv`  
- **Size:** ~2.4MB  
- **Features:** `price`, `bedrooms`, `bathrooms`, `sqft_living`, `floors`, `zipcode`, etc.  
- **Target:** `price`

---

## 🧠 Models Applied

- **Linear Regression**
- **Gradient Boosting Regressor (XGBoost)**

---

## 🛠 Project Structure

```
House Price Prediction/
│
├── house_price_model.ipynb          # Jupyter notebook for training and evaluation
├── kc_house_data.csv                # Dataset
├── requirements.txt                 # Python dependencies
├── README.md                        # Project overview
│
├── results/
│   └── house_price_predictions.xlsx # Output file with actual vs predicted prices
│
└── src/
    ├── preprocessing.py             # Functions for data loading & cleaning
    ├── model.py                     # Model training and prediction logic
    └── visualization.py             # Plots and visualizations
```

---

## 📈 Key Results

| Metric            | Linear Regression | XGBoost |
|-------------------|------------------:|--------:|
| MAE               | ~121,000          | ~83,000 |
| RMSE              | ~153,000          | ~104,000 |

*(Note: Exact values may vary depending on preprocessing.)*

---

## 📌 How to Run

1. Clone this repository.
2. Open the `house_price_model.ipynb` notebook in Jupyter or VS Code.
3. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Run all the cells to load data, preprocess, train, evaluate, and export predictions.

---

## 👩‍💻 Author

**Aafia Azhar**  
GitHub: [@aafia1](https://github.com/aafia1)

---

## 📁 Output

The predicted results are saved as:  
`results/house_price_predictions.xlsx`
