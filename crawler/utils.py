import datetime
import requests

def get_year(next=True):
    today = datetime.date.today()

    year = today.year
    
    return year + 1 if next else year

def check_url_exit(url):
    response = requests.get(url)
    return response.status_code == 200