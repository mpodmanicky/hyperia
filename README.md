# Zadanie
Parsovanie dát zo stránky prospektmaschine.de


Vytvor konzolový skript v Pythone verzie 3+, ktorý dokáže rozparsovať stránku https://www.prospektmaschine.de/hypermarkte/ a stiahnuť zoznam aktuálne platných letákov pre všetkých 40+ reťazcov v danej kategórií. Výstup ulož do súboru v JSON formáte.


Dodržuj prosím formáty dátumov tak ako je uvedené v príklade.


Príklad výstupného formátu:
[
	{
		“title”: “Prospekt”,
		“thumbnail”: “https://eu.leafletscdns.com/…04818/0.jpg”,
		“shop_name”: “Aldi”,
		“valid_from”: “2025-02-17”,
		“valid_to”: “2025-02-22”,
		“parsed_time”: “2025-02-17 20:00:00”
},
...
]


Pri implementácií sa sústreď na stabilitu riešenia a dátovú konzistentnosť. Zaujíma nás tvoj prístup k OOP,  čistote, prehľadnosti kódu ako aj dodržiavaní štandardov.


Zadanie prosím odovzdaj ako link na repozitár u tvojho obľúbeného poskytovateľa (Gitlab, Github, Bitbucket, …)

### Pre spustenie
`pip3 install requests beautifulsoup4`

potom

`python3 script.py`
