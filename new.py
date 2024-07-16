from sqlalchemy import create_engine, Column, Integer, String, Numeric, text
from sqlalchemy.orm import declarative_base, sessionmaker
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Database connection parameters
db_type = 'postgresql'
username = 'postgres'
password = 'riaRome1705'
host = 'localhost'
port = '5432'
database = 'postgres'

# Create the connection string
connection_string = f"{db_type}://{username}:{password}@{host}:{port}/{database}"
print(f"Connecting to: {connection_string}")  # For debugging

# Create the engine
engine = create_engine(connection_string)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define the ORM model for the airports table with schema
class Airport(Base):
    __tablename__ = 'airports'
    __table_args__ = {'schema': 'project_2'}
    
    airport_id = Column(Integer, primary_key=True)
    iata_code = Column(String(3))
    airport = Column(String(100))
    city = Column(String(100))
    state = Column(String(2))
    country = Column(String(10))
    latitude = Column(Numeric)
    longitude = Column(Numeric)

# Create the table in the database (if it doesn't exist)
Base.metadata.create_all(engine)
print("Table 'airports' checked/created successfully in schema 'project_2'")

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Fetch data from the 'airports' table using ORM
airport_data = []
try:
    # Query the data using ORM
    airports = session.query(Airport).all()

    if airports:
        # Convert the query result to a list of dictionaries
        airport_data = [
            {
                'airport_id': a.airport_id,
                'iata_code': a.iata_code,
                'airport': a.airport,
                'city': a.city,
                'state': a.state,
                'country': a.country,
                'latitude': a.latitude,
                'longitude': a.longitude
            }
            for a in airports
        ]

        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(airport_data)

        # Display the DataFrame
        print("Data in 'airports' table in schema 'project_2':")
        print(df)
    else:
        print("No data found in 'airports' table in schema 'project_2'.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    session.close()

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the Dash app
app.layout = html.Div([
    html.H1("Airports Dashboard"),
    dcc.Graph(id='bar-chart'),
    html.Div([
        html.H2("Airports Data"),
        html.Table([
            html.Thead(html.Tr([html.Th(col) for col in df.columns])),
            html.Tbody([
                html.Tr([
                    html.Td(df.iloc[i][col]) for col in df.columns
                ]) for i in range(min(len(df), 10))  # Limit to first 10 rows
            ])
        ])
    ])
])

# Callback to update the bar chart
@app.callback(
    Output('bar-chart', 'figure'),
    Input('bar-chart', 'id')
)
def update_bar_chart(_):
    fig = px.bar(df, x='iata_code', y='latitude', hover_name='airport',
                 title="Airports Latitude by IATA Code")
    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)