import requests
import bs4

loops = 0
visted = []
site = "https://misec.us"

def getLinks(link, loops):
  
  if link in visted:
    return 0
  if site not in link: #stay on target site
    return 0  
  r = requests.get(link)
  soup = bs4.BeautifulSoup(r.text, 'html.parser')  
  visted.append(link) # track where we've already been
  if len(visted) % 10 == 0: 
    print("loops: " + str(loops) + "pages crawled: "+ str(len(visted)) )
  links = soup.find_all('a')
  loops += 1
  if loops == 900:
    return 0
  for link in links:
    try:
     link['href']
    except: 
      continue    
    getLinks(link['href'], loops)
  loops -= 1  
    
getLinks(site, loops)   
print("total pages: "+ str(len(visted)) )
