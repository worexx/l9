from aiohttp import web
import asyncio

fileRoute = "./static/index.html"


async def handle(request):
    text = "Привет от Димы! "
    answer = ""
    with open(fileRoute, 'r') as f:
        answer += f.read()
    return web.Response(text=text + answer, content_type="text/html")

app = web.Application()
app.add_routes([web.get('/', handle)])

if __name__ == '__main__':
    web.run_app(app)
