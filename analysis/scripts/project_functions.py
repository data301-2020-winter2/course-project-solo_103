import matplotlib.pyplot as plt
import seaborn as sns
import pandas_profiling as pdp
import pandas as pd
import numpy as np

def load_and_process(path):
    df1=(pd.read_csv(path).dropna()
    .reset_index()
    .drop(columns="index"))
    
    df2=(df1
    .rename(columns = {"artist_name":"Artist","track_name":"Title","release_date":"Year"})
    .drop(columns=["Unnamed: 0","lyrics","age","len"])
    .assign(Decade=df["Year"]-df["Year"]%10)
   )
    return df2
