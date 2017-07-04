import requests
import json
from flask import Flask
from flask import render_template
app = Flask(__name__)

def crawl_tuch(searchTerm="", page="1"):
    imageurl = 'http://tuchong.com/rest/search/posts?query={}&count=30&page={}'.format(searchTerm, page)
    head = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-GB,en;q=0.5', 'Connection': 'keep-alive',
            'Cookie': 'webp_enabled=0; log_web_id=5000125721', 'DNT': '1', 'Host': 'tuchong.com', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/4.0 (Windows NT 07.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/53.0'}
    conn = requests.get(imageurl, headers=head)
    tuch_net = conn.json()
    
    ###Parse Tuch
    tuch_loc = {}
    resp = tuch_net["data"]["post_list"]
    for range1 in range(0, len(resp)):
        for k, v in resp[range1].items():
            lenvar2 = (resp[range1]["images"])
            for range2 in range(0, len(lenvar2)):
                c_item= lenvar2[range2]
                # if lenvar2[range2]["width"] > 800 and lenvar2[range2]["height"] > 800:
                if c_item["img_id"] not in tuch_loc:
                    tuch_loc[(c_item["img_id"])]={"title": c_item["title"], "desc": c_item["excerpt"], "usr_id": c_item["user_id"], "thumb": c_item["source"]["ft640"], "img": c_item["source"]["l"]}
    return tuch_loc


def crawl_adesk(searchTerm=""):
    url = 'http://so.picasso.adesk.com/v1/search/wallpaper/resource/{}?limit=100&channel=androidesk&adult=true&first=1&order=hot'.format(searchTerm)
    salt = {'host': 'so.picasso.adesk.com', 'connection': 'Keep-Alive', 'user-agent': "picasso,174,androidesk", 'Accept-Encoding': 'gzip'}
    conn = requests.get(url, headers=salt)
    adesk_net = conn.json()
    ###Parse Adesk
    adesk_out = {}
    resp = adesk_net["res"]["wallpaper"]
    for range1 in range(0, len(resp)):
        c_item= resp[range1]
        if resp[range1]["id"] not in adesk_out.keys():
            try:
                adesk_out[str(c_item["id"])]= {"title": "rank: "+ str(c_item["rank"]), "desc":"favs: "+ str(c_item["favs"]), "usr_id": c_item["user"]["name"], "thumb": c_item["thumb"], "img": c_item["wp"]}
            except KeyError as e:
                print(e)
                continue
    return adesk_out


def sagramour_crawl(searchTerm="", page="1"):
    tuch_out= crawl_tuch(searchTerm, page)
    adesk_out= crawl_adesk(searchTerm)
    tuch_out.update(adesk_out)
    return tuch_out


@app.route('/<searchTerm>/<page>')
def crawl_this(searchTerm, page):
    return render_template("index.html", imageDict=sagramour_crawl(searchTerm, page))

if __name__ == "__main__":
    app.run(debug=True)