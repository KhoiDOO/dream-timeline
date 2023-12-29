import os, sys
from typing import Any
import requests
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self, url) -> None:
        self.__url = url
        self.__url_text = self.__download_url(self.__url)
        self.__html_parser = self.__get_parser(self.__url_text)
        self.__text = self.__html_parser.get_text()
        self.__tag = self.__html_parser.b 
    
    def __download_url(self, url):
        return requests.get(url).text        

    def __get_parser(self, html):
        return BeautifulSoup(html, 'html.parser')
    
    def __call__(self) -> Any:
        raise NotImplementedError

    def get_url(self):
        return self.__url
    
    def get_url_text(self):
        return self.__url_text
    
    def get_text(self):
        return self.__text
    
    def get_html_parser(self):
        return self.__html_parser
    
    def get_tag(self):
        return self.__tag