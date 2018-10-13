#!/usr/bin/python
# python3+
from itertools import *
from bisect import *
import sys
def is_palindrome(i):
	a = str(i)
	return a == a[::-1]

bits = range(25)

def comb_to_int(comb):
	# print (comb)
	return sum(map(lambda x: 10**x, comb))

def comb_to_string(comb):
	return str(comb_to_int(comb))

valids = ['1','2','3'] # the square roots of fair+square numbers
valids.extend('2' + x + '2' for x in ['','0','1']) #empty comb	
valids.extend('2' + '0'*i + '2' for i in range(2,49))
valids.extend('2' + '0'*i + '1' + '0'*i +'2' for i in range(1,24))

#for p in ('2' + '0'*i + '1' + '0'*i +'2' for i in range(1,24)):
#	sys.stderr.write(str(p) + '\n')

for i in range(1,5+1):	
	for comb in map(comb_to_string,combinations(bits, i)):
		valids.extend(comb + x + comb[::-1] for x in ['','0','1','2'])
		valids.extend('2' + comb + x + comb[::-1] + '2' for x in ['','0','1'])
valids = list(set(map(int,valids)))
valids.sort()

def faq(p):
	return is_palindrome(p) and is_palindrome(p**2)

valids = list(map(lambda k: k**2, filter(faq, valids)))

#for v in valids:
#	sys.stderr.write(str(v) + '\n')

def get_left_index(x):
	i = bisect_right(valids,x)
	return i-1

def get_right_index(x):
	i = bisect_left(valids, x)
	return i

# sys.stderr.write('reading now\n')
t = int(sys.stdin.readline())
for case in range(t):
	s = sys.stdin.readline().split()
	a, b = tuple(map(int,s))
	c = get_left_index(a)
	d = get_right_index(b)
	extra = 0
	if (valids[c] == a):
		extra = extra + 1
	if (valids[d] == b):
		extra = extra + 1
#	sys.stderr.write(str(a) + ' --> ' + str(c) + '\n')
#	sys.stderr.write(str(b) + ' --> ' + str(d) + '\n')
	print ('Case #%i: %i' % ( case+1, d-c-1 + extra ))
