from re import *
from sys import stderr
def readint():
	return int(raw_input())
def readfloat():
	return float(raw_input())
def readarray(N, foo=raw_input):
	return [foo() for i in xrange(N)]
def readlinearray(foo=int):
	return map(foo, raw_input().split())

def NOD(a, b):
	while b:
		a,b = b, a%b
	return a

def gen_primes(max):
	primes = [1]*(max+1)
	for i in range(2, max+1):
		if primes[i]:
			for j in range(i+i, max+1, i):
				primes[j] = 0
	primes[0] = 0
	return [x for x in range(max+1) if primes[x]]

def is_prime(N):
	i = 3
	if not(N % 2):
		return 0
	while i*i < N:
		if not(N % i):
			return 0
		i += 3
	return 1

def is_live(i):
	return i==1 or i==2

def step(field):
	for i in xrange(1,len(field)):
		for j in xrange(1,len(field[i])):
			if field[i][j] == 1 and (is_live(field[i-1][j]) or is_live(field[i][j-1] > 0)):
				field[i][j] = 1
			elif (is_live(field[i-1][j]) and is_live(field[i][j-1])):
				field[i][j] = 3
			elif field[i][j]:
				field[i][j] = 2
	for i in xrange(1, len(field[0])):
		if not(is_live(field[0][i-1])):
			field[0][i] = 0
	for i in xrange(1,len(field)):
		if not(is_live(field[i-1][0])):
			field[i][0] = 0
	field[0][0] = 0
	count = 0
	for i in xrange(1,len(field)):
		for j in xrange(1,len(field[i])):
			if field[i][j] == 1 or field[i][j] == 3:
				count += 1
				field[i][j] = 1
			else:
				field[i][j] = 0
	return count

case_number = readint()
for case in xrange(case_number):
	R = readint()
	field = []
	points = []
	maxx, maxy = 0,0
	for i in xrange(R):
		x1,y1,x2,y2 = readlinearray()
		maxx,maxy=max(maxx,x2), max(maxy,y2)
		points.append([x1,y1,x2,y2])
	for i in xrange(maxy+1):
		field.append([0]*(maxx+1))
	for p in points:
		for i in xrange(p[0]-1,p[2]):
			for j in xrange(p[1]-1,p[3]):
				field[j][i] = 1
	count = 0
	while step(field):
		count += 1
	print >>stderr, case
	print "Case #%s: %s" % (case + 1, count+1)
