import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")
sub_df = df[["Mortality rate, infant (per 1,000 live births)","GDP per capita (constant 2010 US$)","Country Name"]]
plt.plot(sub_df["GDP per capita (constant 2010 US$)"],sub_df["Mortality rate, infant (per 1,000 live births)"],'o')
plt.xlabel("GDP per capita (constant 2010 US$)")
plt.ylabel("Mortality rate, infant (per 1,000 live births)")
plt.show()