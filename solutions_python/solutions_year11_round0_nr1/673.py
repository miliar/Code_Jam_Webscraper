#!/usr/bin/env python3

import sys
from time import sleep
from threading import Thread


# O2 B3 B4 O3 O5
m = lambda x: x if x>0 else -x

def algoritm(v):

	#print("##", v)
	O = [i[1] for i in v if i[0] == 'O']
	B = [i[1] for i in v if i[0] == 'B']

	D = {'O': [], 'B': []}

	for i in range(len(O)):
		if not i: D['O'].append(m(O[i]-1))
		else: D['O'].append(m(O[i]-O[i-1]))

	for i in range(len(B)):
		if not i: D['B'].append(m(B[i]-1))
		else: D['B'].append(m(B[i]-B[i-1]))

	t = 0
	k = 0

	while D['O'] or D['B']:
		d = {'O':False, 'B':False}
		t += 1
		i = v[k]

		for j in D:
			if D[j] and D[j][0] > 0:
				D[j][0] -= 1
				d[j] = True

		if D[i[0]][0] == 0 and not d[i[0]]:
			D[i[0]].pop(0)
			k += 1

	return t

class Proc(Thread):
	def __init__(self, param, case):
		Thread.__init__(self, name=str(case))

		p = param.split()
		n = int(p.pop(0))
		self.opt = [(p[i], int(p[i+1])) for i in range(0, 2*n, 2)]
		self.r = 0
		print("@@", self.opt)

	def run(self):
		self.r = algoritm(self.opt)


def main():
	with open('A-large.in', 'r') as S:
		I = S.readlines()
		N = int(I.pop(0))

	O = open('large.out', 'w')

	print("$$", I, N)
	T = []

	for i in range(N):
		p = Proc(I[i].strip(), case=i)
		p.start()
		T.append(p)

	while any([i.is_alive() for i in T]):
		sleep(2)
		R = [(i.name, i.r) for i in T if i.is_alive()]
		print("&&", len(R), R)

	for i in T:
		O.write("Case #{0}: {1}\n".format(int(i.name)+1, i.r))
	O.close()

if __name__ == '__main__':
	main()
	sys.exit(0)
