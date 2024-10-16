from bs4 import BeautifulSoup


async def parse_info(text:str):
    soup = BeautifulSoup(text,"html.parser")

    developer = soup.find("th",text="Developer").find_next("td").text
    os = soup.find("th",text="OS").find_next("td").text
    license = soup.find("th",text="License").find_next("td").text

    return {"Developer":developer,
            "OS":os,
            "License":license}
