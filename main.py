from fastapi import FastAPI,Request,status
from fastapi.responses import RedirectResponse
import requests
from bs4 import BeautifulSoup

async def get_url(url):
    req = requests.get(url).content
    soup = BeautifulSoup(req,'html.parser')
    title = soup.find("h3",{"class":"dwnldFilename"}).text
    link = soup.find("source",{"type":"video/mp4"})['src']
    created_time = soup.find('td',{"align":"center"}).text.replace("Time: ","")
    resp = requests.head(link)
    size = int(resp.headers.get('Content-Length',0))
    return {"title":title, "size":size, "link":link,"created_time":created_time}

app = FastAPI()


@app.get("/")
async def read_root():
    return RedirectResponse(url="https://github.com/iseshu/pdisk-api/", status_code=status.HTTP_302_FOUND)

@app.get('/get')
async def api(request: Request):
    a = request.query_params.get('url')
    data = await get_url(a)
    return data
