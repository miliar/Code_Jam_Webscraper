import sys
import os

def transform_number(nombre):
	n = len(nombre)
	for i in range(n-1):
		if (nombre[i+1]<nombre[i]):
			nbb = int(nombre[i])
			nombre[i] = str(nbb-1)
			for j in range(i+1, n):
				nombre[j] = str(9)

			return True

	return False



	return need_to
t = int(input())

for i in range(t):
	nb = input()
	nombre = list(nb)

	while(True):
		if not transform_number(nombre):
			break



	sol = ''.join(nombre)
	print("Case #" + str(i+1) + ": ", end="")
	print(int(sol))