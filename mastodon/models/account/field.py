from typing import Optional
from datetime import datetime

from pydantic import AnyHttpUrl

from mastodon.models import MastodonModel


class Field(MastodonModel):
    """
    Mastodon :class:`.Account` fields.

    In the source, currently commented out, is the capacity
    to also represent any URLs that are present in the
    field, but it requires BeautifulSoup so I've left it out
    for this limited demo.
    """
    name: str
    value: str
    verified_at: Optional[datetime] = None
    # url: Optional[AnyHttpUrl] = None

    # def __init__(self, name:str, value:str):
    #     soup = BeautifulSoup(value, 'lxml')
    #     a = soup.find('a')
    #     if a is not None:
    #         url = a.get('href')
    #     else:
    #         url = None
    #     super().__init__(name=name, value=value, url=url)

    # class Config:
    #     extra = "ignore"