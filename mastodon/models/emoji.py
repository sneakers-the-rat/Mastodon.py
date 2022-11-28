from typing import Optional

from pydantic import HttpUrl

from mastodon.models import MastodonModel


class Emoji(MastodonModel):
    shortcode: str
    url: HttpUrl
    static_url: HttpUrl
    visible_in_picker: bool
    category: Optional[str] = None
