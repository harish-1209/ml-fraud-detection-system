import pandas as pd


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform basic preprocessing on fraud dataset.

    Steps:
    - Convert datetime column
    - Create time-based features
    - Create age from DOB
    - Drop unnecessary columns

    Args:
        df (pd.DataFrame): Raw dataset

    Returns:
        pd.DataFrame: Cleaned dataset
    """

    df = df.copy()

    # Convert datetime
    df["trans_date_trans_time"] = pd.to_datetime(df["trans_date_trans_time"])

    # Extract time features
    df["trans_hour"] = df["trans_date_trans_time"].dt.hour
    df["trans_dayofweek"] = df["trans_date_trans_time"].dt.dayofweek
    df["trans_month"] = df["trans_date_trans_time"].dt.month

    # Convert DOB to datetime
    df["dob"] = pd.to_datetime(df["dob"])

    # Create age feature
    df["age"] = df["trans_date_trans_time"].dt.year - df["dob"].dt.year

    # Drop columns not useful for modeling
    drop_cols = [
        "first",
        "last",
        "street",
        "trans_num",
        "cc_num"
    ]

    df = df.drop(columns=[col for col in drop_cols if col in df.columns])

    return df