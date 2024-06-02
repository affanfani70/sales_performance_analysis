import pandas as pd

def load_sales_data(csv_file_path):
    """
    Load sales data from a CSV file.
    """
    return pd.read_csv(csv_file_path)
