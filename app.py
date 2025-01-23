import datetime

from litestar import Litestar, get


@get("/params")
async def params(
    some_date: datetime.date | None = None, some_bool: bool | None = None
) -> str:
    if some_date:
        return "Great date!"
    if some_bool:
        return "Great bool!"
    return "No params?"


app = Litestar([params])
