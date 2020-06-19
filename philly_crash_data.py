import pandas as pd
import geopandas as gpd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns


def philly_crash_data():
    csv_filepath = "data/simplified_data.csv"

    philly_data = pd.read_csv(csv_filepath)
    philly_data = philly_data.sort_values('crash_year', ascending=False)

    print(philly_data)

philly_crash_data()


