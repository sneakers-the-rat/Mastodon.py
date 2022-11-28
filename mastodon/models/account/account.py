from datetime import datetime
from typing import Optional, List, ClassVar, Literal

from pydantic import AnyHttpUrl, EmailStr, HttpUrl
from pydantic import Field as _Field

from mastodon.models import MastodonModel
from mastodon.models.account.field import Field
from mastodon.models.emoji import Emoji

PRIVACY = Literal[
    'privacy',
    'unlisted',
    'public'
]

class Source(MastodonModel):
    privacy: PRIVACY = _Field(
        description= "The user's default visibility setting (\"private\", \"unlisted\" or \"public\")"
    )
    sensitive: bool = _Field(
        description="Denotes whether user media should be marked sensitive by default"
    )
    note: str = _Field(
        description="Plain text version of the user's bio"
    )

class Account(MastodonModel):
    id: int = _Field(
        description = "Same as <numerical id>"
    )
    username: str = _Field(
        description = "The username (what you @ them with)"
    )
    acct: EmailStr = _Field(
        description = "The user's account name as username@domain (@domain omitted for local users)"
    )
    avatar: HttpUrl = _Field(
        description="URL for their avatar, can be animated"
    )
    avatar_static: HttpUrl = _Field(
        description="URL for their avatar, never animated"
    )
    bot: bool = _Field(
        description="Boolean indicating whether this account is automated."
    )
    created_at: datetime = _Field(
        description="Account creation time"
    )
    discoverable: bool = _Field(
        description="Indicates whether or not a user is visible on the discovery page"
    )
    display_name: str = _Field(
        description="The user's display name"
    )
    emojis: List[Emoji] = _Field(
        default_factory=list,
        description="List of custom emoji used in name, bio or fields"
    )
    fields: List[Field] = _Field(
        default_factory=list,
        description=(
            "List of up to four dicts with free-form 'name' and 'value' profile info. "
            "For fields with \"this is me\" type verification, verified_at is set to the "
            "last verification date (It is None otherwise)"
        )
    )
    followers_count: int = _Field(
        description="How many followers they have"
    )
    following_count: int = _Field(
        description="How many people they follow"
    )
    group: bool = _Field(
        description="A boolean indicating whether the account represents a group rather than an individual"
    )
    header: HttpUrl = _Field(
        description="URL for their header image, can be animated"
    )
    header_static: HttpUrl = _Field(
        description="URL for their header image, never animated"
    )
    locked: bool = _Field(
        description="Denotes whether the account can be followed without a follow request"
    )
    moved_to_account: Optional['Account'] = _Field(
        default=None,
        description="If set, a user dict of the account this user has set up as their moved-to address."
    )
    note: str = _Field(
        description="Their bio"
    )
    source: Optional[Source] = _Field(
        default=None,
        description="Additional information - only present for user dict returned from account_verify_credentials()"
    )
    statuses_count: int = _Field(
        description="How many statuses they have"
    )
    url: AnyHttpUrl = _Field(
        description="Their URL; for example 'https://mastodon.social/users/<acct>'"
    )

    @classmethod
    def from_list(cls, accounts:List[dict]) -> List['Account']:
        return [Account(**account) for account in accounts]
