#!/urs/bin/python

import sys

# @param f: file handler
# @param n: number of lines to be read
def readnl(f, n):
	lines = []
	for i in range(n):
		lines.append(f.readline())

	return lines

# checks if a output filename was given, if it wasn't a file with sufix ".answer" is generated
def getOutputHandler(target = ''):
	if target == 'stdout':
		return sys.stdout
	elif (len(sys.argv) >= 3):
		out = file(sys.argv[2], "w")
	else:
		out = file(sys.argv[1] + '.answer', 'w')

	return out

def getInputHandler(source = ''):
	if source == 'stdin':
		return sys.stdin
	elif (len(sys.argv) < 2):
		print "NO INPUT FILE!"
		exit()

	return file(sys.argv[1])

def resetHash(hash, default):
	for i in hash.keys():
		hash[i] = default

def lowerAlphabet():
  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	return map(chr, range(97, 123))

def upperAlphabet():
	# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	return map(chr, range(65, 91))

def wholeAlphabet():
	return lowerAlphabet() + upperAlphabet()

# Dictionary Stuff
def find_key(dic, val):
	return [k for k, v in dic.iteritems() if v == val][0]

def readHash(f, n, default):
	hash = {} 
	for i in range(n):
		hash[f.readline()] = default 

	return hash

def time2minutes(time):
	tokens = time.split(':')
	return int(tokens[0]) * 60 + int(tokens[1])

def time2seconds(time):
	tokens = time.split(':')
	return int(tokens[0])*3600 + int(tokens[1])*60 + int(tokens[2])

# times in seconds
def addMin(time, min):
	[h, m] = time.split(':')
	m = int(m)

	if (m + min >= 60):
		h = str(int(h) + 1)

	if int(h) < 10 and h[0] != '0':
		h = '0' + h

	mm = ''

	m = (m + min) % 60

	if m == 0:
		mm = '00'
	elif (m > 0 and m < 10):
		mm = '0' + str(m)
	else:
		mm = str(m)

	return h + ':' + mm

def factorial(n):
	assert n > 0, 'factorial: n must be greater than 0'
	fact = 1

	if n > 1:
		for i in range(2, n+1):
			fact *= i
	
	return fact

def all_perms(str):
	if len(str) <=1:
		yield str
	else:
		for perm in all_perms(str[1:]):
			for i in range(len(perm)+1):
				yield perm[:i] + str[0:1] + perm[i:]
