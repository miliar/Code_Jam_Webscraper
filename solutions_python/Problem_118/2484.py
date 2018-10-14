## CodeJam 2013
## Brian Hernandez

from sys import argv
from math import sqrt

def isPal(otroNum):
	## regresa True si otroNum es palindromo
	normalNum = str(otroNum)
	if(len(normalNum) == 1):
		## todos los numeros de 1 digito son palindromos
		return True
	reverseNum = normalNum[::-1]
	if(normalNum == reverseNum):
		return True

def test(number):
	hijo = sqrt(number)
	if(hijo.is_integer()):
		hijo = int(hijo)
		if(isPal(hijo) and isPal(number)):
			return 1
	return 0

def solve(a, b, salida, caso):
	num = a
	total = 0
	while(num <= b):
		total += test(num)
		num += 1
	salida.write("Case #%d: %d\n" % (caso, total))

f = open(argv[1], "r")
veces = f.readline()

salida = open("salida.txt", "w")

for caso in range(int(veces)):
	numbers = f.readline()[:-1].split(" ")
	a = int(numbers[0])
	b = int(numbers[1])
	solve(a, b, salida, caso+1)

f.close()
salida.close()
