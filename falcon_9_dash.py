# Import required libraries
import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the data
spacex_df = pd.read_csv("spacex_launch_dash.csv")

# Max and min payload for slider
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Get unique launch sites for Falcon 9 launches (using Booster Version Category to identify Falcon 9)
# According to your CSV, Booster Version Category column values are like 'v1.0', 'v1.1', 'FT', 'B4', 'B5'
# Assuming all are Falcon 9 related; if not, you can adjust filter accordingly
falcon9_categories = spacex_df['Booster Version Category'].unique()
falcon9_df = spacex_df[spacex_df['Booster Version Category'].isin(falcon9_categories)]

# Unique launch sites for dropdown
launch_sites = falcon9_df['Launch Site'].unique().tolist()

# Dropdown options including 'All Sites'
dropdown_options = [{'label': 'All Sites', 'value': 'ALL'}] + \
                   [{'label': site, 'value': site} for site in launch_sites]

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),

    # TASK 1: Dropdown for Launch Site selection
    dcc.Dropdown(
        id='site-dropdown',
        options=dropdown_options,
        value='ALL',
        placeholder='Select a Launch Site here',
        searchable=True,
    ),
    html.Br(),

    # TASK 2: Success pie chart
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    # TASK 3: Payload slider
    dcc.RangeSlider(
        id='payload-slider',
        min=min_payload,
        max=max_payload,
        step=1000,
        marks={int(i): str(int(i)) for i in range(int(min_payload), int(max_payload)+1, 2000)},
        value=[min_payload, max_payload]
    ),
    html.Br(),

    # TASK 4: Scatter plot for payload vs launch success
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])


# TASK 2 Callback: update pie chart based on selected site
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def update_pie_chart(selected_site):
    if selected_site == 'ALL':
        # Use all data
        filtered_df = spacex_df
        # Count success launches by site
        fig = px.pie(
            filtered_df,
            names='Launch Site',
            values='class',
            title='Total Successful Launches by Site'
        )
    else:
        # Filter data for the selected site
        filtered_df = spacex_df[spacex_df['Launch Site'] == selected_site]
        # Count success and failure for that site
        success_counts = filtered_df['class'].value_counts().reset_index()
        success_counts.columns = ['class', 'count']
        # Rename 1 as Success, 0 as Failure
        success_counts['class'] = success_counts['class'].map({1: 'Success', 0: 'Failure'})
        fig = px.pie(
            success_counts,
            names='class',
            values='count',
            title=f'Success vs Failure Launches for site {selected_site}'
        )
    return fig


# TASK 4 Callback: update scatter plot based on site and payload slider
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [
        Input(component_id='site-dropdown', component_property='value'),
        Input(component_id='payload-slider', component_property='value')
    ]
)
def update_scatter_chart(selected_site, payload_range):
    low, high = payload_range
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)]
    if selected_site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == selected_site]
    fig = px.scatter(
        filtered_df,
        x='Payload Mass (kg)',
        y='class',
        color='Booster Version Category',
        title='Payload vs. Launch Success',
        labels={'class': 'Launch Outcome (1=Success, 0=Failure)'}
    )
    return fig


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
