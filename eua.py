import pandas as pd

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'

#importing table
df = pd.read_csv(url)
print(df)
df.to_excel('confirmed_cases_us.xlsx')