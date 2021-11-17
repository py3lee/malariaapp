import dash
from dash import (
    dcc,
    html
)
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
from pathlib import Path
import pandas as pd

df_path = Path(__file__).parents[1] / 'data/processed/malaria_deaths_age_processed.csv'
df = pd.read_csv(df_path)

all_age_group = df.age_group.unique()
all_entity_type = df.entity_type.unique()

entity_type_options = dbc.Container(
    [
        dbc.Row([html.Div("""by entity types:""")]),
        dcc.RadioItems(
            id="entity_type",
            options=[{"label": x, "value": x} for x in all_entity_type],
            value=all_entity_type[0],
            labelStyle={'display': 'inline-block'},
            inputStyle={
                "margin-right": "5px", 
                "margin-left": "10px",
                "margin-top": "10px"
            },
            style = {'text-align': 'left'}
        )
    ]
)

age_group_options = dbc.Container(
    [
        dbc.Row([html.Div("""by age groups:""")]),
        dcc.RadioItems(
            id="age_group",
            options=[{"label": x, "value": x} for x in all_age_group],
            value=all_age_group[0],
            labelStyle={'display': 'inline-block'},
            inputStyle={
                "margin-right": "5px", 
                "margin-left": "10px",
                "margin-top": "10px"
                }
        )
    ],
    style={"height": "10vh"}
)

subset_options = dbc.Container(
    [
        dbc.Row([html.H3("Explore the data")]),
        dbc.Col([entity_type_options, age_group_options])
    ],
    style={"height": "20vh"}
)

body = dbc.Container(
    [
        dbc.Row(
            [html.H1("Visualization of malaria datasets")], 
            justify="center", 
            align="center", 
            className="h-50"
        ),
        subset_options,
        dcc.Graph(id="line-chart")
    ],
    style={"height": "20vh"}
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])
app.layout = body

@app.callback(
    Output("line-chart", "figure"), 
    Input("entity_type", "value"),
    Input("age_group","value")
)
def update_line_chart(
    all_entity_type, 
    all_age_group
):
    entity_type_mask = df.entity_type.isin([all_entity_type])
    age_group_mask = df.age_group.isin([all_age_group])

    fig = px.line(
        df[entity_type_mask & age_group_mask], 
        x="year", 
        y="deaths", 
        color="entity",
        title = "Number of malaria deaths from 1990 - 2016",
        labels={
            "year": "Year",
            "deaths": "Number of malaria deaths",
        }
    )
    return fig

server = app.server
app.run_server(debug=True)