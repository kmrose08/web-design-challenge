import pandas as pd

df = pd.read_csv("cities.csv")
html = df.to_html('data.html')
