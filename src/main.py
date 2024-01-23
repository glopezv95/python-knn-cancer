import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

from data import variables
from callbacks import generate_callbacks
app = dash.Dash(external_stylesheets = [dbc.themes.BOOTSTRAP])  

app.layout = dbc.Container(children = [
    dcc.Dropdown(id = 'hist_dd', options = variables, value = 'Radius'),
    html.H3(id = 'hist_title'),
    dcc.Graph(id = 'hist_graph'),
    html.P(id = 't_test_p')
])

generate_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug = True)