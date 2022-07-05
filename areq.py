import asyncio
import aiohttp
from aiohttp import ClientSession


async def fetch_url(url: str, session: ClientSession) -> str:
    response = await session.request(method="GET", url=url)
    response.raise_for_status()
    text = await response.text()
    print(text.strip())

async def get_url():
    async with ClientSession() as session:
        tasks = []
        for i in range(50):
            tasks.append(
                fetch_url("https://commitment.herokuapp.com/txt", session)
            )
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(get_url())
