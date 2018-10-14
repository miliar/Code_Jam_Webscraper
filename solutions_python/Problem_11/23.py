#!/usr/bin/python

import sys
import string
from sets import Set
import psyco
psyco.full()
from psyco.classes import *

ugly = [2, 3, 5, 7]

symbols = ["X", "+", "-"]

nlist = []

def blah(number):

	global nlist
	
	if len(number) == 1:
		num = number.pop(0)
		nlist.append(num)
		return
		
	num = number.pop(0)
	blah(number)
	nlist2 = nlist
	
	# add all possible symbol combinations
	nlist = []
	for i in nlist2:
		
		# add nothing
		#nstr = str(num) + i
		#nlist.append(nstr)
		nlist.append(str(num) + i)
		# add plus
		#nstr = str(num) + "+" + i
		#nlist.append(nstr)
		nlist.append(str(num) + "+" + i)		
		# add minus
		#nstr = str(num) + "-" + i
		#nlist.append(nstr)
		nlist.append(str(num) + "-" + i)
		
	return

def countUglies(number):

	count = 0
	blah(number)
	print "length: " + str(len(nlist))
	
	# now cycle through nlist and determine if a numebr is ugly
	for nstr in nlist:
	
		#print "Checking: " + str(nstr)
		
		a = ""
		val = 0
		op = ""

		for x in xrange(0, len(nstr)):

			j = nstr[x]

			if j == '+' or j == '-':

				if len(a) > 0 and op == "":
					val = int(a)
				elif len(a) > 0 and op == "+":
					val = val + int(a)
				elif len(a) > 0 and op == "-":
					val = val - int(a)
				else:
					print "Error: trying to convert string: " + nstr
					
				a = ""
			else:
				a = a + j

			if j == '+':
				op = "+"
			elif j == '-':
				op = "-"
			
		# at the end of the string, perform last operation
		if op == "+":
			val = val + int(a)
		elif op == "-":
			val = val - int(a)
		else:
			val = int(a)
		
		
		# now we have a value, is it ugly?
		for d in ugly:
			if val % d == 0:
				count = count + 1
				break
		
		
	return count
	
# usage: problem <input file> <output file>
if len(sys.argv) != 3:
	print "usage: problem <input file> <output file>"
	sys.exit()

inputfile = sys.argv[1]
outputfile = sys.argv[2]

# open the input file and read in the contents
infile = open(inputfile, "r")
outfile = open(outputfile, "w")

# read in the number of test cases
N = int(infile.readline())
print "The number of test cases is: " + str(N)
curCase = 1
for i in xrange(1, N+1):


	line = infile.readline().strip()
	numbers = list(line)
	
	print "Numbers: " + str(numbers)

	nlist = []
	count = countUglies(numbers)

	outfile.write("Case #%d: %d\r\n" % (curCase, count))
	curCase = curCase + 1


infile.close()
outfile.close()