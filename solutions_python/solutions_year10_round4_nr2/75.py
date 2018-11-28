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

def get_left_part(tree):
	res = []
	for i in xrange(len(tree)-1):
		res.append(tree[i][:len(tree[i])/2])
	return res
def get_right_part(tree):
	res = []
	for i in xrange(len(tree)-1):
		res.append(tree[i][len(tree[i])/2:])
	return res

def answer(costs, _M):
	#if 2**len(costs) != len(_M):
		#print costs, _M
		#exit()
	if len(costs) == 1:
		if _M[0] and _M[1]:
			return 0
		else:
			return costs[0][0]
	res = costs[len(costs)-1][0] + answer(get_left_part(costs), _M[:len(_M)/2]) + answer(get_right_part(costs), _M[len(_M)/2:])
	if not(0 in _M):
		M = [x-1 for x in _M]
		res1 = answer(get_left_part(costs), M[len(M)/2:])+answer(get_right_part(costs), M[:len(M)/2])
		res = min(res, res1)
	return res

case_number = readint()
for case in xrange(case_number):
	P = readint()
	M = readlinearray()
	costs = [readlinearray() for i in xrange(P)]
	res = answer(costs, M)
	#if case == 6 or case < 5:
		#print M
	#if case == 6:
		#exit
	print >>stderr, case
	print "Case #%s: %s" % (case + 1, answer(costs, M))
