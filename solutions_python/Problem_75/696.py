#!/usr/bin/env python3

import sys
from time import sleep
from threading import Thread

def mag(C, D, Q):
	R = ''
	while Q:
		R += Q.pop(0)
		for c in C:
			R = R.replace(c[:2], c[2])
			R = R.replace(''.join(reversed(c[:2])), c[2])
		for d in D:
			if d[0] in R and d[1] in R:
				print("¬¬", R)
				R = ''
	return(list(R))

class Proc(Thread):
	def __init__(self, param, case):
		Thread.__init__(self, name=str(case))

		self.C = []
		self.D = []
		p = param.split()

		for i in range(int(p.pop(0))):
			self.C.append(p.pop(0))

		for i in range(int(p.pop(0))):
			self.D.append(p.pop(0))

		p.pop(0)

		self.Q = list(p.pop(0).strip())

		self.r = 0

	def run(self):
		self.r = mag(self.C, self.D, self.Q)


def main():
	with open('B-large.in', 'r') as S:
		I = S.readlines()
		N = int(I.pop(0))

	O = open('large.out', 'w')

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
		r = str(i.r).replace("'", "")
		O.write("Case #{0}: {1}\n".format(int(i.name)+1, r))
	O.close()

if __name__ == '__main__':
	main()
	sys.exit(0)
