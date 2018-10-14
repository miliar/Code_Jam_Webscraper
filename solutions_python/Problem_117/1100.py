#!/usr/bin/python

import sys

if len(sys.argv) != 2:
    print "Please run program: python file.py inputFilename"
    sys.exit()

try:
    f = open(sys.argv[1],'r')
    count = int(f.readline())
except IOError:
    print "Input File could not be opened"
    sys.exit()

case = 1

while count > 0:#{

	line = f.readline();
	if not line:
		f.close()
		break

	#print line
	val = line.split(' ')
	#print val
	N = int(val[0])
	M = int(val[1])

	i = 0
	data = []
	while i < N:

		line = f.readline()
		if not line:
			f.close()
			break
		#print line
		line.rstrip()
		line = [int(n) for n in line.split()]
		data.append(line)

		i = i + 1

	#print data
	
	answer = "YES"
	while(True):
		'''
		'''

		#remove empty Rows and columns
		k = 0
		while k < len(data):

			if len(data[k]) == 0:
				del data[k]
				continue
			k = k + 1

		if len(data) == 0:
			break

		min_val = 99999
		minr = 0
		minc = 0

		r = 0
		while r < len(data):
			c = 0
			while c < len(data[r]):
				if min_val > data[r][c]:
					min_val = data[r][c]
					minc = c
					minr = r
				c = c + 1
			r = r + 1

		numc = 0
		numr = 0
		rb = True
		cb = True

		j = 0
		#print data
		while j < len(data[minr]):
			if data[minr][j] == min_val:
				numr = numr + 1

			j = j + 1

		if numr != len(data[minr]):
			rb = False

		j = 0
		while j < len(data):
			if data[j][minc] == min_val:
				numc = numc + 1

			j = j + 1

		if numc != len(data):
			cb = False


		if rb  == False and cb == False:
			answer = "NO"
			break

		if cb:

			j = 0
			while j < len(data):
				del data[j][minc]
				j = j + 1
			continue

		elif rb:
			del data[minr]
			continue


	print "Case #" + str(case) + ": " + answer
	case = case + 1
	count = count - 1


#}









