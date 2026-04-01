import pandas as pd
from pathlib import Path


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file

    Returns:
        pd.DataFrame: Loaded dataset
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(path)
    return df


def load_train_data(config: dict) -> pd.DataFrame:
    """
    Load training dataset based on config.

    Args:
        config (dict): Configuration dictionary

    Returns:
        pd.DataFrame
    """
    train_path = config["data"]["train_path"]
    return load_csv(train_path)


def load_test_data(config: dict) -> pd.DataFrame:
    """
    Load test dataset based on config.

    Args:
        config (dict): Configuration dictionary

    Returns:
        pd.DataFrame
    """
    test_path = config["data"]["test_path"]
    return load_csv(test_path)