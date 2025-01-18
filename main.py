from dash import Dash, html, dcc, callback, Output, Input 
import plotly_express as px
import plotly.graph_objects as go
import pandas as pd
import get_data 

ticker_list = get_data.get_coins_list()
period_list = ['1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max']
interval_list = ['2h','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo']
app = Dash()

app.layout = (
    html.Div(
        [
    
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(ticker_list,'BTC-USD', id='ticker'),
    dcc.Dropdown(period_list,'max',id='period'),
    dcc.Dropdown(interval_list,'1d',id='interval'),
    dcc.Graph(
        id='graph-content',
        config={"scrollZoom": True}
        )
        ])
)
@callback(
    Output('graph-content', 'figure'),
    Input('ticker', 'value'),
    Input('period','value'),
    Input('interval','value')
)

def update_graph(ticker_value,period_value,interval_value):
    coin_data = get_data.get_coin(ticker_value,period_value,interval_value)
    coin_data["Open"] = coin_data["Open"].interpolate()
    coin_data["High"] = coin_data["High"].interpolate()
    coin_data["Low"] = coin_data["Low"].interpolate()
    coin_data["Close"] = coin_data["Close"].interpolate()
    fig = go.Figure(
        go.Candlestick(
            x=coin_data.index,
            open=coin_data["Open"],
            high=coin_data["High"],
            low=coin_data["Low"],
            close = coin_data["Close"],
        ),
    )
    fig.update_layout(
        xaxis_rangeslider_visible=False,
        autosize=False,  
        height=800,
        plot_bgcolor="black",
        dragmode="pan", 
        xaxis=dict(showgrid=True, gridwidth=1, gridcolor='gray'),
        yaxis=dict(
            showgrid=True, 
            gridwidth=1, 
            gridcolor='gray'
            )
    )
    return fig
   
if __name__ == "__main__":
    app.run(debug=True)