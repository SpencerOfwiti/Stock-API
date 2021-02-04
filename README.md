# Stock API

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0) 
![GitHub repo size](https://img.shields.io/github/repo-size/SpencerOfwiti/Stock-API.svg)
![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)
[![contributors](https://img.shields.io/github/contributors/SpencerOfwiti/Stock-API.svg)](https://github.com/SpencerOfwiti/stock-ml/contributors)

A python UWSGI server for availing stock predictions to external clients. It contains two submodules that generate stock price predictions:
StockMl - Predictions based on historical data,
Sentiment Analysis - Prediction based on market confidence in publications.
* [API address](http://45.63.97.7:9090): http://45.63.97.7:9090
* [Predictions endpoint](http://45.63.97.7:9090/predictions): /predictions

## Table of contents
* [Motivation](#motivation)
* [Built With](#built-with)
* [Submodules](#submodules)
* [Code Example](#code-example)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Tests](#tests)
* [Deployment](#deployment)
* [Contributions](#contributions)
* [Bug / Feature Request](#bug--feature-request)
* [Authors](#authors)
* [License](#license)

## Motivation

This project was born out of the need to make financial literacy and investment options available for the common citizen.
Over the years the number of individuals investing in the Kenyan Securities Market has reduced.
More and more of the trading is being done by investment companies and wealthy investors.
This provides a platform to lower the barriers to entry for everyone keen on investing in the securities market. 
It provides daily predictions on the stock price for the next day and an overview of what to expect in the coming week.


## Built With
* [Python 3.8](https://www.python.org/) - The programming language used.
* [Pytest](https://docs.pytest.org/en/latest/) - The testing framework used.

## Submodules
* [StockML](https://github.com/SpencerOfwiti/StockML) - Implementation of various machine learning algorithms in the prediction of Kenya's stock market performance. 
* [SentimentAnalysisStockML](https://github.com/Minjire/sentiment_analysis_stock_ml.git) - Implementation of various machine learning algorithms in the prediction of Kenya's stock market performance.

## Code Example

```python
def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'Hello World!']
```

## Prerequisites

What things you need to install the software and how to install them

* **python 3**

Linux:
```
sudo apt-get install python3.8
```

Windows:

Download from [python.org](https://www.python.org/downloads/windows/) 

Mac OS:
```
brew install python3
```

* **pip**

Linux and Mac OS:
```
pip install -U pip
```

Windows:
```
python -m pip install -U pip
```

## Installation

Clone this repository while updating submodules:
```
git clone --recurse-submodules https://github.com/SpencerOfwiti/Stock-API
```

To set up virtual environment and install dependencies:
```
source setup.sh
```

To run web server:
```
uwsgi --http :9090 --wsgi-file server.py
```

To update submodules:
```
git submodule update --remote <submodule_name>
```

## Tests

This system uses pytest to run automated tests.

To run automated tests:
```
pytest
```

## Deployment

Add additional notes about how to deploy this on a live system

## Contributions

To contribute, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).


## Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/SpencerOfwiti/Stock-API/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/SpencerOfwiti/Stock-API/issues/new). Please include sample queries and their corresponding results.

## Authors

* **[Spencer Ofwiti](https://github.com/SpencerOfwiti)**
    
[![github follow](https://img.shields.io/github/followers/SpencerOfwiti?label=Follow_on_GitHub)](https://github.com/SpencerOfwiti)
[![twitter follow](https://img.shields.io/twitter/follow/SpencerOfwiti?style=social)](https://twitter.com/SpencerOfwiti)

* **[Kelvin Minjire](https://github.com/Minjire)**
  
[![github follow](https://img.shields.io/github/followers/Minjire?label=Follow_on_GitHub)](https://github.com/Minjire)
[![twitter follow](https://img.shields.io/twitter/follow/minjirekelvin?style=social)](https://twitter.com/minjirekelvin)

* **[Kevin Wachira](https://github.com/wachira-kevin)**

[![github follow](https://img.shields.io/github/followers/wachira-kevin?label=Follow_on_GitHub)](https://github.com/wachira-kevin)


## License

This project is licensed under the GNU General Public License V3.0 - see the [LICENSE.md](LICENSE.md) file for details
