import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_and_clean_data(path):
    df = pd.read_csv(path)
    df = df.dropna()
    return df

def preprocess_features(df):
    df = df.copy()
    le = LabelEncoder()
    if 'zipcode' in df.columns:
        df['zipcode'] = le.fit_transform(df['zipcode'])
    features = df[['sqft_living', 'bedrooms', 'bathrooms', 'zipcode']]
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    return scaled_features, df['price']