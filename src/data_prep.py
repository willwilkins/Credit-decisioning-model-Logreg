import pandas as pd
import numpy as np

from ucimlrepo import fetch_ucirepo

def load_uci_data(dataset_id):
    """Load data from UCI ML Repository."""
    data = fetch_ucirepo(id=dataset_id)
    return data.data.features, data.data.targets

def clean_data(df):
    """Handle missing values, duplicates, etc."""
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def engineer_features(df):
    """Create new features or transform existing ones."""
    # Your transformations
    return df