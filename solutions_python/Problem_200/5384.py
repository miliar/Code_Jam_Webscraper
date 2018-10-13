#!/usr/bin/python

import os
import sys
import string
import re


def process (text):

	s = ""

	lines = text.split("\n")
	while "" in lines:
		lines.remove("")

	N = None
	i = 1
	for line in lines:
		#print line
		if i == 0:
			pass
		elif i == 1:
			N = str(line)
		else:
			print ">>>>> " + str(i-1)
			n = line
			r = calc_grande(int(n), 3)
			s += "Case #%d: %s\n" % (i-1, r)
		i += 1

	return s


def calc_grande (n, lim):

	print n

	lim = 3

	cad = ""	

	s = str(n)

	while True:

		#print "s: " + s

		#if s == "0"*len(s):
		#	cad += "9"*(len(s)-1)
		#	break
		#elif len(s) > lim:
		if len(s) > lim:
			ll = len(s) - lim
			#print "s[ll:]: " + s[ll:]
			r = calc(int(s[ll:]))
			#print "r: " + str(r)
			s2 = "0"*(len(s[ll:])-len(str(r))) + str(r)[::-1]
			#print "s2: " + str(s2)
			#for i in range(len(s2)):
			salir = False
			c = ""
			i = 0
			s2_ = s2[::-1]
			#print "s2_: " + s2_
			if s2_ == "0"*len(s2_):
				cad = "9"*(len(s2_)-1) + cad
				i = len(s2_)
			else:
				while not salir and i<len(s2_):
					#print "s2_[" + str(i) + "]: " + s2_[i]
					if int(s2_[i]) == 9:
						c += s2_[i]
					else:
						salir = True
					i += 1
			cad = c[::-1] + cad
			s = s[:ll] + "0"*(len(s2_)-i+1)
			#print "cad: " + cad
			#break
		else:
			r = calc(int(s))
			cad = str(r) + cad
			#print "## cad: " + cad
			break

	print cad

	return cad


def calc (n):

	last = None

	tidy = 1

	#print n
	#for i in range(1, n+1):
	i = n
	while i<=n and i>0:
		#print "  i: " + str(i)
		tidy = 1
		l = 0
		for j in str(i):
			#print "    j: " + str(j)
			if int(j) < l:
				tidy = 0
				break
			l = int(j)
		if tidy:
			last = i
			break
		i -= 1
		#next

	if tidy:
		last = i

	#print "last: " + str(last)

	return last


def calc_mal (n):

	last = None

	#print n
	#for i in range(1, n+1):
	i = 1
	while i <= n:
		#print "  i: " + str(i)
		tidy = 1
		l = 0
		#for j in str(i):
		lj = range(len(str(i)))
		j = 0
		while j < len(str(i)) and tidy:
			#print "    j: " + str(j)
			if int(lj[j]) < l:
				tidy = 0
				break
			l = j
			j += 1
		if tidy:
			last = i
		i += 1
		#next

	print "last: " + str(last)

	return last


def calc_no_optimo (n):

	last = None

	i = 1
	while i <= int(n):
		l = list(str(i))
		print "l: " + str(l)
		ls = l[:]
		ls.sort()
		print "ls: " + str(ls)
		if l == ls:
			last = i
		i += 1

	print "last: " + str(last)

	return last


if __name__ == "__main__":

	( inputfile, ) = sys.argv[1:]

	inpt = """4
132
1000
7
111111111111111110
"""

	inpt = open(inputfile, "r").read()
	outputfile = inputfile + ".out"
	out = process(inpt)
	outpt = open(outputfile, "w")
	outpt.write(out)
	outpt.close()

	#for i in (5, 0, 1, 2 , 11, 1692):
	#	print ">>>>>> %d" % i
	#	print calc(i)

