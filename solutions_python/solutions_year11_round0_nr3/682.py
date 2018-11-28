#!/usr/bin/env python3

import sys
from time import sleep
from threading import Thread

from itertools import combinations
from operator import xor

#T = {}

def Sum(l):
	"""Return Patrick's sum of all elements in l tuple"""
	if len(l) == 0: return 0
	elif len(l) == 1: return l[0]
	elif len(l) == 2: return xor(l[0], l[1])
	else:
		return xor(Sum(l[:-1]), l[-1])

def Lsub(a, b):
	a = list(a)
	for i in b:
		if i in a:
			a.remove(i)
	return a

def Candy(C):
	#print("@@", C)
	v = 0
	C.sort()
	L = len(C)

	for j in range(1, int(L/2)+(L%2)+1):
		for i in combinations(C, j):
			k = tuple(Lsub(C, list(i)))
			if not k or not i: print("00", C, i, k)
			r = Sum(i)
			s = Sum(k)
			m = max([sum(i), sum(k)])
			if r == s and m > v:
				v = m

	return v

class Proc(Thread):
	def __init__(self, param, case):
		Thread.__init__(self, name=str(case))

		self.p = [int(i) for i in param.split()]
		self.r = 0

	def run(self):
		self.r = Candy(self.p)

def main():
	with open('C-small-attempt2.in', 'r') as S:
		L = S.readlines()
		N = int(L.pop(0).strip())

	I = [L[2*i+1] for i in range(N)]

	O = open('small.out', 'w')

	T = []

	for i in range(N):
		p = Proc(I[i].strip(), case=i)
		p.start()
		T.append(p)

	while any([i.is_alive() for i in T]):
		sleep(2)
		#R = [(i.name, i.r) for i in T if i.is_alive()]
		#print("&&", len(R), R)

	for i in T:
		if not i.r: r = "NO"
		else: r = i.r
		O.write("Case #{0}: {1}\n".format(int(i.name)+1, r))
	O.close()

if __name__ == '__main__':
	main()
	sys.exit(0)
