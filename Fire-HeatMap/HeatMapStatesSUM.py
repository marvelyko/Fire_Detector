import plotly.express as px
from plotly.offline import plot
import pandas as pd

url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
df = pd.read_csv(url, converters={'fips': lambda x: str(x)})

url = "https://raw.githubusercontent.com/jasonong/List-of-US-States/master/states.csv"
df_abbrev = pd.read_csv(url)

last_date = df['date'].max()
df = df[ df['date'] == last_date]
df = df.groupby('state')['cases'].sum().to_frame()
df = pd.merge(df, df_abbrev, left_on=df.index, right_on='State')

fig = px.choropleth(df, locations=df['Abbreviation'], color=df['cases'],
                    locationmode="USA-states",
                    color_continuous_scale="magma",
                    range_color=(0, 50000),
                    scope="usa"
                    )

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
plot(fig)