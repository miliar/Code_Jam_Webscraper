
from math import sqrt, fmod

fprint = open("resultado.txt", 'a');
fraw_input = open("entrada.txt", 'r');

def isPalindrome(n):
	n = str(n)
	j = 0
	if(fmod(float(n), 1.0) != 0.0):
		return False
	n = str(int(float(n)))
	siz = len(n)
	for i in range(siz):
		j = j - 1
		if(n[i] != n[j]):
			return False
	return True

t = 0
a = 0
b = 0
lis = []
cant = 0

t = int(fraw_input.readline())
for i in range(t):
	cant = 0
	lis = fraw_input.readline().split(' ')
	a = int(lis[0])
	b = int(lis[1])
	for j in range(a, b + 1):
		if(isPalindrome(j) and isPalindrome(sqrt(j))):
			cant = cant + 1
	
	fprint.write("Case #" + str(i + 1) + ": " + str(cant) + "\n")
			
