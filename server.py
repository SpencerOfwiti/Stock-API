import json
from typing import Optional, Union
from urllib.parse import urlparse, parse_qs
from StockML.src.predictions import get_predictions
from sentiment_analysis_stock_ml.src.sentiment.predictions import get_sentiment_predictions


def get_query_parameters(env: dict, query_name: Optional[str] = None) -> Union[dict, str]:
    """
    Gets value of the request query parameters.
    :param env: Object containing server and request information
    :type env: dict
    :param query_name: The specific query parameter to fetch.
    :type query_name: str
    :return: Query parameters from the request.
    :rtype: dict | str
    """
    parsed_url = urlparse(env.get('REQUEST_URI'))
    params = parse_qs(parsed_url.query)
    if query_name:
        param = params.get(query_name)[0]
        return param
    return params


def get_request_endpoint(env: dict) -> str:
    """Gets value of the request url path.
    :param env: Object containing server and request information
    :type env: dict
    :return: Endpoint that has been touched by the call
    :rtype: str
    """
    return env.get('PATH_INFO')


def get_request_method(env: dict) -> str:
    """Gets value of the request method.
    :param env: Object containing server and request information.
    :type env: dict
    :return: Request method.
    :rtype: str
    """
    return env.get('REQUEST_METHOD').upper()


def application(env: dict, start_response: any):
    """
    Loads python code for application to be accessible over web server.
    :param env: Query parameters from the request.
    :type env: dict
    :param start_response: Callable to define responses.
    :type start_response: any
    """
    # define headers
    errors_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', '0'),
    ]
    headers = [
        ('Content-Type', 'application/json'),
        ('Access-Control-Allow-Origin', '*')
    ]

    response = b'Hello World!'

    # validate request method
    if not get_request_method(env) == 'GET':
        start_response('405 Play by the rules', errors_headers)
        return []

    if get_request_endpoint(env) == '/predictions':
        historical_data = 'StockML/data/interim/Safaricom-Ltd(SCOM).csv'
        predictions_data = 'StockML/data/predicted/lstm/Safaricom-Ltd(SCOM).csv'
        sentiment_predictions_data = 'sentiment_analysis_stock_ml/data/predicted/safaricom_predictions.csv'
        history, predictions = get_predictions(historical_data, predictions_data)
        sentiment_predictions = get_sentiment_predictions(sentiment_predictions_data)
        sentiment = 'Neutral'
        if len(sentiment_predictions) > 0:
            ratio = max(sentiment_predictions)
            if ratio is sentiment_predictions[0]:
                sentiment = 'Negative'
            elif ratio is sentiment_predictions[2]:
                sentiment = 'Positive'
        response = {
            "company": 'Safaricom',
            "predictions": predictions,
            "sentiment_predictions": sentiment_predictions,
            "sentiment": sentiment,
            "history": history
        }
        response = json.dumps(response)
        response_bytes = str(response).encode('utf-8')
        start_response('200 OK', headers)
        return [response_bytes]

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [response]
