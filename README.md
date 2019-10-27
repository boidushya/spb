# ShitPostBot downloader
A script that downloads shitpostbot source images according to query you provide
# Requirements
  * [Python3](https://www.python.org/downloads/)
  * BeautifulSoup
    ```python
    pip install beautifulsoup4
    ```
  * Requests
    ```python
    pip install requests
    ```
  * lxml
    ```python
    pip install lxml
    ``|


# Usage:
```
python fetch.py -q [query]
```
If you want a random image, just type
```
python fetch.py -q --rand
```
By default the script sends you a random image from the list of the received query.
If you want to get the only the top post and nothing less, use:
```
python fetch.py -q [query] --top
```
