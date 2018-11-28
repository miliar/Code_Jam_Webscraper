#!/usr/env/bin/ python

from math import sqrt

def palindromic_check(n):
	o = str(n)
	if o == o[::-1]:
		return True
	return False


source='C-small-attempt0.in'

def find_square_palindromes(filename):
	f=open(source)
	n = int(f.readline())
	i = 1
	while i<n+1:
		counter = 0
		line = f.readline()
		a = int(line.split()[0])
		b = int(line.split()[1])
		for num in range(a,b+1):
			if palindromic_check(num):
				root = sqrt(num)
				if root == int(root):
					if palindromic_check(int(root)):
						counter+=1
		print "Case #" + str(i) +": " + str(counter)
		i+=1

find_square_palindromes(source)