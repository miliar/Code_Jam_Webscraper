#/usr/bin/python

def vrati_ne_samoglasnik(rijec):
	if rijec == 'a' or rijec == 'o' or rijec == 'e' or rijec == 'i' or rijec == 'u':
		return 0
	return 1

def get_broj_slova(rijec,broj):
	#print rijec
	skup = 0
	for i in range(0,len(rijec)):
		if vrati_ne_samoglasnik(rijec[i]) == 1:
			skup+=1
			if skup == broj:
				#print rijec
				return 1
		else:
			skup =0
	return 0

def get_n_value(rijec,broj):
	rjesenje = 0
	for i in range(0,len(rijec)-broj+1):
		brojac = broj-2

		while (i+brojac) < (len(rijec)):
			#print str(brojac) + " brojac"
			brojac+=1
			if len(rijec[i:(i+brojac)]) < broj:
				continue

			if get_broj_slova(rijec[i:(i+brojac)],broj):
				#print rijec[i:(i+brojac)]
				rjesenje+=1

	return rjesenje


datoteka = open("test1","r")
datoteka.readline()
brojac = 0
for t in datoteka:
	brojac+=1
	k = t.split()
	rijec = k[0]
	broj_ponavljanja = int(k[1])

	broj = get_n_value(rijec,broj_ponavljanja)

	print "Case #" + str(brojac) + ": " + str(broj)