import requests
def getHTML(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "error"
    
if __name__ == "__main__":
    url = "http://www.bing.com"
    print(getHTML(url))