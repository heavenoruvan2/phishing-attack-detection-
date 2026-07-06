def extract(url):
 return [len(url),1 if url.startswith("https") else 0,url.count("."),url.count("-"),1 if "@" in url else 0]
