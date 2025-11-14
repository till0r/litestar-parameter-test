import datetime
from dataclasses import dataclass
from typing import Annotated

from litestar import Litestar, get
from litestar.params import Parameter


@dataclass
class ParameterSet:
    some_date: datetime.date | None = None
    some_bool: bool | None = None


DTorNone = datetime.date | None


@get("/params")
async def params(query: dict) -> str:
    print(query)
    if query.get("some_date"):
        some_date = query.get("some_date")
        return f"Great date! {some_date}!"
    return "No params?"


app = Litestar([params])
