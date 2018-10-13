import sys

f = open('c-small-attempt0.in')
s = open("salida2.txt","w")
n = int(f.readline())

pares = []
for i in range(n):
	pares.append(f.readline())

for j in range(n):
	numeros = pares[j].split()
	contador = 0
	k = int(numeros[0])
	while k < int(numeros[1]):
		for i in range(len(numeros[0])):
			m = int(str(k)[i:] + str(k)[:i])
			if (k < m and int(m) <= int(numeros[1])):
				contador += 1
		k += 1
	s.write("Case #" + str(j+1) + ": " + str(contador) + "\n")
