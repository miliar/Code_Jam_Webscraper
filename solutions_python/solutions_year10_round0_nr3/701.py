#!/bin/python
import pickle
def skaityk_skaiciu(failas):
	rez = ""
	while True:
		laik = failas.read(1)
		if (laik == ' ') or (laik == '\n'):	
			break
		else:
			rez = rez + laik
	return int(rez)
def sudeliok_indeksus(skaic, k):
	laik = [-1, -1]
	rez = []
	for a in range(len(skaic)):
		rez.append(laik)
	nuo = 0
	i = 0
	suma = 0
	while True:
		if ((skaic[i] + suma) > k)or((i == nuo)and(suma != 0)):
			laik = [suma, i]
			rez[nuo] = laik
			if rez[i][0] != -1:
				return rez
			i = i - 1
			suma = 0
			nuo = i+1
		else:
			suma = suma + skaic[i]
		i = i + 1
		if i >= len(skaic):
			i = 0
	return rez
f = open('test.in', 'r')
f2 = open('test2.out', 'w');
a = f.readline()
a = int(a);
for i in range(a):
	eile = []
	R, k, N = skaityk_skaiciu(f), skaityk_skaiciu(f), skaityk_skaiciu(f)
	for u in range(N):
		eile.append(skaityk_skaiciu(f))
	ind = sudeliok_indeksus(eile, k)
	suma = 0
	kk = 0
	for u in range(R):
		suma = suma + ind[kk][0]
		kk = ind[kk][1]
	rezstr = 'Case #{0}: {1}\n'.format(i+1, suma)
	f2.write(rezstr)
print a

