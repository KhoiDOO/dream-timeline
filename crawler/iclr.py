from typing import Any
from .core import Crawler
from .utils import get_year, check_url_exit

base_url = "https://iclr.cc/Conferences/{}/CallForPapers"

class ICLR(Crawler):
    def __init__(self, url = None) -> None:
        if url is not None:
            super().__init__(url)
        else:
            url = base_url.format(get_year(next=True))
            if check_url_exit(url):
                self.__current_year = get_year(next=True)
                super().__init__(url)
            else:
                self.__current_year = get_year(next=False)
                url = base_url.format(self.__current_year)
                super().__init__(url)

    def __call__(self) -> Any:
        
        base_html_parser = self.get_html_parser()
        
        title = base_html_parser.title.string
        
        event_date = base_html_parser.h4.string
        
        main_dict = {
            "Title" : title,
            "Event Date" : event_date,
        }
        
        important_date_str = base_html_parser.find_all("ul")[-3].get_text().strip().split("\n")
        
        important_dates = [dates.split(": ", maxsplit = 1) for dates in important_date_str]
        
        important_dates_dct = {
            text[0] : text[1] for text in important_dates
        }
        
        main_dict.update(important_dates_dct)
        
        return main_dict