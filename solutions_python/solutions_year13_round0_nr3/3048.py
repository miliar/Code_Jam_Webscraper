#!/usr/bin/python
import os
import io
import sys
import math

def test():
	i = 0
	j = 1
	string = sys.stdin.readline().strip('\n')
	t = int(string)
	for string in sys.stdin.readlines():
		mytab = list()
		somme = 0
		for char in string.strip('\n').split(' ', string.count(' ')):
			mytab.append(char)
		a = int(mytab[0])
		b = int(mytab[1])
		for i in range(a,b+1):
			if str(i) == str(i)[::-1] and math.sqrt(i) == int(math.sqrt(i)):
				if str(int(math.sqrt(i))) == str(int(math.sqrt(i)))[::-1]:			
					somme+=1
		print ("Case #{0}:").format(j), somme
		j+=1		

if __name__ == "__main__":

	test()
