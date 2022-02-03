import csv
import re
import os 
import orodja

mapa = "kraji"
mapa_tabele = "obdelani_podatki"
csv_datoteka = "podatki.csv"

vzorec = (
    r'<figure id="attachment_\d*" .*?'
    r'class="wp-caption-text">Source: .*?'
    r'class="wp-caption-text">'
    r'(?P<kraj>.*?)</figcaption></figure>\n'
    r'(?P<opis>(<p>.*</p>\n)*)'
)

#vsebina = orodja.preberi_file(mapa, "Laos.html")
#seznam_krajev = []
#for zadetek in re.finditer(vzorec, vsebina):
#    slovar = dict()
#    slovar['kraj'] = zadetek.group('kraj')
#    slovar['opis'] = zadetek.group('opis').replace('<p>', '').replace('</p>\n', ' ')
#    seznam_krajev.append(slovar)
#print(seznam_krajev)
#    

def ustvari_seznam_krajev():
    seznam_krajev = []

    for ime_datoteke in os.listdir(mapa):
        vsebina = orodja.preberi_file(mapa, ime_datoteke)
        
        for zadetek in re.finditer(vzorec, vsebina):
            slovar = dict()
            slovar['kraj'] = zadetek.group('kraj')
            slovar['opis'] = zadetek.group('opis').replace('<p>', '').replace('</p>\n', ' ')
            seznam_krajev.append(slovar)
    return seznam_krajev
    
orodja.naredi_csv(
    ['kraj', 'opis'],
    ustvari_seznam_krajev(),
    mapa_tabele,
    csv_datoteka
)