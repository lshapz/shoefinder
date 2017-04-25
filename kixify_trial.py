import requests, sys, webbrowser, bs4
print('Kicking off...')    # display text while downloading the Google page
res = requests.get('https://www.kixify.com/search?s=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)
# Open a browser tab for each result.
print(soup)
linkElems = soup.select('.product-title a')

numOpen = min(10, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://www.kixify.com' + linkElems[i].get('href'))