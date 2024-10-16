from aiohttp import ClientSession
from pydantic import HttpUrl
from . import parse_info
from . import app


@app.get("/parsing")
async def parse(web_site:HttpUrl):
    async with ClientSession() as session:
        resp=await session.get(f"{web_site}")
        info = await resp.text()
        parsed_info=await parse_info(info)
        return parsed_info