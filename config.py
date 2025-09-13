import os
DASH_APP_NAME = 'dash-stock-tickers-app'
DASH_APP_PRIVACY = 'public'
PATH_BASED_ROUTING = True
os.environ['PLOTLY_USERNAME'] = 'your-plotly-username'
os.environ['PLOTLY_API_KEY'] = 'your-plotly-api-key'
os.environ['PLOTLY_DOMAIN'] = 'https://your-plotly-domain.com'
os.environ['PLOTLY_API_DOMAIN'] = os.environ['PLOTLY_DOMAIN']
PLOTLY_DASH_DOMAIN='https://your-dash-manager-plotly-domain.com'
os.environ['PLOTLY_SSL_VERIFICATION'] = 'True'