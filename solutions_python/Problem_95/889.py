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

from string import lowercase

s1 = 'aozejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv'
s2 = 'yeqour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up'

m = {}
for i in xrange(len(s1)):
    m[s1[i]] = s2[i]

m[set(lowercase).difference(set(s1)).pop()] = set(lowercase).difference(set(s2)).pop()

case_number = readint()
for case in xrange(case_number):
    a = ''.join(map(lambda c: m[c], raw_input()))
    print "Case #%s: %s" % (case + 1, a)
