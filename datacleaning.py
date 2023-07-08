import pandas as pd

data = pd.read_csv('final.csv')

del data["Star_name"]
data = data.dropna()

data.to_csv("final2.csv")