import re
import csv

key1 = 'href="/watch'
key2 = '"'
f = open('prova.txt',encoding='utf8')
g = str(f.readlines())

lista = []
for match in re.finditer(key1, g): # per ogni link di youtube
	inizio = match.start() # posizione del link di youtube
	fine = g.find(';',inizio) # posizione finale del link di youtube
	fine2 = g.find('"',inizio+6) # posizione finale della stringa di youtube

	index0 = g.find('index=',inizio) # posizione iniziale della stringa index
	if g[index0+6].isnumeric():
		fine_index = re.search("\D", g[index0+6:index0+20]).start() # trova il primo val non numerico dopo "index="
		index = g[index0+6:index0+6+fine_index] # trovami index, da "index=" a x

		link = 'youtube.com' + g[inizio+6:fine]

		el = [link,index]
		if el not in lista:
			lista += [el]

print(lista)
f.close()

header = ['Link', 'Indice']

with open('prova.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f, delimiter=';')

    writer.writerow(header)
    writer.writerows(lista)
