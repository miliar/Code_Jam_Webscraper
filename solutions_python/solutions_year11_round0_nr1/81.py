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

case_number = readint()
for case in xrange(case_number):
	s = raw_input().split()
	steps = zip(s[1::2], s[2::2])
	blue_pos = 1
	blue_time = 0
	orange_pos = 1
	orange_time = 0
	time = 0
	for step in steps:
		pos = int(step[1])
		if step[0]== 'B':
			time += max((blue_time - time + abs(pos - blue_pos)), 0) + 1;
			blue_time = time;
			blue_pos = pos;
		else :
			time += max((orange_time - time + abs(pos - orange_pos)), 0) + 1;
			orange_time = time;
			orange_pos = pos;
	print "Case #%s: %s" % (case + 1, time)
