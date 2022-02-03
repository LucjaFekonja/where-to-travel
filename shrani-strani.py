import re
import requests 
import orodja

STEVILO_STRANI = 439
mapa_krajev = 'kraji'

def nalozi_stran(url):
    print(f'Nalagam {url}...')
    headers = {'Accept-Language': 'de-at;it-it;en-us'}
    odziv = requests.get(url, headers=headers)
    return odziv.text

vzorec = (
    r'<h2 class="entry-title" '
    r'itemprop="headline">'
    r'<a href="(?P<url>.*?)"'
    r' rel="bookmark">'
    r'\d* .*? to Visit in (?P<drzava>.*?)'
    r'</a></h2>'
)

st = 0
for stran in range(200, STEVILO_STRANI):
    url = f'https://www.thecrazytourist.com/page/{stran}/'
    #vsebina = nalozi_stran(url)
    #with open(f'page-{stran}.html', 'w', encoding='utf-8') as f:
    #    f.write(vsebina)

    with open(f'page-{stran}.html', encoding='utf-8') as f:
        vsebina = f.read()

        for zadetek in re.finditer(vzorec, vsebina):
            url = zadetek.group('url')
            ime_datoteke = zadetek.group('drzava') + ".html"
            orodja.shrani_stran(url, mapa_krajev, ime_datoteke)
            print(zadetek.groupdict())
print(st)


