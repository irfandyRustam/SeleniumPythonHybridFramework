pytest -v -m "sanity" --html=./Reports/reportSanityChrome.html testCases --browser chrome
:: pytest -v -m "sanity" --html=./Reports/reportSanityFF.html testCases --browser firefox
:: pytest -v -m "regression" --html=./Reports/reportRegression.html testCases --browser chrome
:: pytest -v -m "sanity or regression" --html=./Reports/report.html testCases --browser chrome
:: pytest -v -m "sanity and regression" --html=./Reports/report.html testCases --browser chrome