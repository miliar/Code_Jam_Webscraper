#! /usr/bin/python

from sys import argv,exit
from math import sqrt

def palindrome(n):
	s = str(n)
	return s == s[-1::-1]

def not_is_square(n):
	return sqrt(n) != int(sqrt(n))

def square_palindrome(n):
	if not_is_square(n):
		return False
	sq = int(sqrt(n))
	return palindrome(sq)

def analizar_linea(s):
	a = int(s.split(" ")[0])
	b = int(s.split(" ")[1])

	l = [a for a in range(a,b+1) if square_palindrome(a) and palindrome(a)]

	return str(len(l))


if len(argv) != 3:
	print "Usage: prog <filein> <fileout>"
	exit(0)

filein = open(argv[1],"r")
fileout = open(argv[2],"w")

lines = filein.read().split("\n")
nlines = int(lines[0])

for i in range(1,nlines+1):
	fileout.write("Case #" + str(i) + ": ")
	fileout.write(analizar_linea(lines[i]) + "\n")
