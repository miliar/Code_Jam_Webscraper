import math
f = open("input.txt");
lista= []
lista = f.readlines()
n = int(lista[0])
lista.pop(0)
print n
f.close()
f = open("output.txt","w")
final = []
lsf = []

def fair(n):
	b = str(n)
	if b[::-1] == b:
		return 1
	return 0

def build(maximo):
	n = 1
	while (n<=maximo):
		if ((fair(n) == 1) and (fair(n**2))):
			lsf.append(n**2)
		n+=1

build(10**6)
print lsf

def fair_square(cadeia):
	ln = cadeia.split()
	n1 = int(ln[0])
	n2 = int(ln[1])
	contador = 0
	for x in range(n1,n2+1):
		if x in lsf:
			contador += 1
	final.append(contador)

for i in lista:
	fair_square(i)

for i in range(len(final)):
	f.write("Case #" + str(i+1) + ": " + str(final[i]))
	f.write("\n")
