#!/usr/bin/python

import sys
import re

BASE = ['Q','W','E','R','A','S','D','F']
NONBASE = ['B','C','G','H','I','J','K','L','M','N','O','P','T','U','V','X','Y','Z']

class Data():
	def __init__(self,C,D,N):
		self.C = C
		self.flagC = False
		self.D = D
		self.flagD = False
		self.N = N

	def opposed(self):
		self.N.pop(self.p)
		self.N.pop(self.p)

	def combine(self):
		self.N.pop(self.p)
		self.N.pop(self.p)
		self.N.insert(self.p,self.Ccomb)
		

if __name__ == '__main__':
	f = open(sys.argv[1])
	lines = f.readlines()
	f.close()
	
	cases = []
	p = re.compile('\d+\s|\s\d+\s')
	for l in lines[1:]:
		ls = p.split(l[:-1])[1:]
		ll = []
		ll = map(lambda x : x.split(), ls)
		cases.append(ll)
	
	casen = 1
	for case in cases:
		C = []
		for v in case[0]:
			tmp = list(v)
			C.append(tmp)
		D = []
		for v in case[1]:
			tmp = list(v)
			D.append(tmp)
		N = list(case[2][0])

		#print C,D,N

		NN = []
		for n in N:
			NN.append(n)
			if len(NN) > 1:
				for c in C:
					check = [ [c[0],c[1]] , [c[1],c[0]] ]
					if NN[-2:] in check:
						NN = NN[:-2]
						NN.append(c[2])
				for d in D:
					if NN.count(d[0]):
						if NN.count(d[1]):
							NN = []
			#print NN
		s = 'Case #' + str(casen) + ': '
		s += '['
		tmp = ''
		for n in NN:
			tmp += n + ', '
		s += tmp[:-2]
		s += ']'
		print s
		casen += 1
