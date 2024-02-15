import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
import plotly.express as px
import pandas as pd
import numpy as np
import pathlib
import os
import dash

dash_app = dash.Dash(__name__)
app = dash_app.server

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("./data").resolve()

data = pd.read_csv(DATA_PATH.joinpath('results.csv'), header=0)

dash_app.layout = html.Div([
    html.H1(children='Automation Results Elektra Release', style={'textAlign': 'center'}),
    html.Div([dash_table.DataTable(
        data=data.to_dict('records'),
        sort_action='native',
        columns=[
            {'name': 'TENANT', 'id': 'TENANT', 'type': 'any', 'editable': False},
            {'name': 'SOH', 'id': 'SOH', 'type': 'any', 'editable': False},
            {'name': 'ENCODE', 'id': 'ENCODE', 'type': 'text'},
            {'name': 'IDENTIFY', 'id': 'IDENTIFY', 'type': 'text'},
            {'name': 'LOOKUP', 'id': 'LOOKUP', 'type': 'text'},
            {'name': 'SEARCHANDPICK', 'id': 'SEARCHANDPICK', 'type': 'any'},
            {'name': 'INVENTORY', 'id': 'INVENTORY', 'type': 'any'},
            {'name': 'UPDATE_INVENTORY', 'id': 'UPDATE_INVENTORY', 'type': 'any'},
            {'name': 'RECEIVING', 'id': 'RECEIVING', 'type': 'any'},
            {'name': 'SHIPPING', 'id': 'SHIPPING', 'type': 'any'},
            {'name': 'PACKING', 'id': 'PACKING', 'type': 'any'},
            {'name': 'API_CALLS', 'id': 'API_CALLS', 'type': 'any'},
            {'name': 'REASON', 'id': 'REASON', 'type': 'any'},
        ],
        editable=True,
        style_data_conditional=[
                                   {
                                       'if': {'column_id': field_name,
                                              'filter_query': ' {' + field_name + '} eq "PASSED"'},
                                       'color': 'green'
                                   } for field_name in data.columns
                               ]
                               +
                               [

                                   {
                                       'if': {'column_id': field_name,
                                              'filter_query': ' {' + field_name + '} eq "FAILED"'},
                                       'color': 'red'
                                   } for field_name in data.columns
                               ]
                               +
                               [

                                   {
                                       'if': {'column_id': field_name,
                                              'filter_query': ' {' + field_name + '} eq "Missing"'},
                                       'color': 'skyblue'
                                   } for field_name in data.columns
                               ]
    )]),
    # dcc.Dropdown(data.TENANT.unique(), 'CENT', id='dropdown-selection'),
    # dcc.Graph(id='graph-content')
])


@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    map_color = {"PASSED": "green", "FAILED": "red", "BORDERLINE": "blue"}
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(data.columns),

                    align='left'),
        cells=dict(values=data,
                   line_color='darkslategray',
                   align='left',
                   font_color=['darkslategray', 'darkslategray', ['green' if x in "PASSED" else
                                                                  "red" if x in "FAILED" else "blue" if x == "BORDERLINE" else 'darkslategray'
                                                                  for x in list(data)]],
                   height=30
                   ))
    ])

    return fig


if __name__ == "__main__":
    dash_app.run_server(debug=True, port=8080)
