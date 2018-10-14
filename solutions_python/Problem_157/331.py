#!/usr/bin/env python
import sys

s = ''
c = 0
rep = 0
multc = {}
forw = []
bacw = []

def mult(n1, n2):
	rlt = ''
	pos = True
	if n1[0] == '-':
		pos = not pos
		n1 = n1[-1]
	if n2[0] == '-':
		pos = not pos
		n2 = n2[-1]
	if n1 == '1':
		rlt = n2
	elif n2 == '1':
		rlt = n1
	elif n2 == n1:
		rlt = '1'
		pos = not pos
	else:
		if (ord(n2) - ord(n1) == -1) or (ord(n2) - ord(n1) == 2):
			pos = not pos
		for n in ['i', 'j', 'k']:
			if n <> n1:
				if n <> n2:
					rlt = n
					break
	if not pos:
		rlt = '-' + rlt
	return rlt
	
def genMultC():
	l = ['1','i','j','k','-1','-i','-j','-k']
	for i in l:
		for j in l:
			multc[(i, j)] = mult(i, j)

def findk(start):
	#print 'finding k', start
	if start >= len(s):
		return 0
	while True:
		tmp = start + 4 * c
		if tmp >= len(s):
			break
		start = tmp
	#print 'finding k', len(s) - start - 1
	if bacw[len(s)-start-1] == 'k':
		return 1
	return 0
	
def findj(start):
	curr = '1'
	for idx in range(start, min(start+4*c,len(s))):
		curr = multc[curr, s[idx]]
		if curr == 'j':
			#print 'j', idx
			if findk(idx + 1) == 1:
				return 1
	return 0
	
def findi():
	curr = '1'
	for idx in range(len(forw)):
		curr = forw[idx]
		if curr == 'i':
			if findj(idx + 1) == 1:
				return 1
	return 0

def process():
	curr = '1'
	found = False
	for i in range(0, min(4*c,len(s))):
		curr = multc[(curr, s[i])]
		if curr == 'i':
			found = True
		forw.append(curr)
	#print forw
	if not found:
		return 'NO'
		
	curr = '1'
	found = False
	for i in range(0, min(4*c,len(s))):
		curr = multc[(s[-1-i], curr)]
		if curr == 'k':
			found = True
		bacw.append(curr)
	#print bacw
	if not found:
		return 'NO'
		
	if findi() == 1:
		return 'YES'
	return 'NO'

genMultC()
#for i in multc:
#	print i, multc[i]
input_file = open(sys.argv[1], 'r')
T = int(input_file.readline())
for i in range(T):
	c, rep = map(int, input_file.readline().split())
	tmp = input_file.readline()
	forw = []
	bacw = []
	s = ''
	for j in range(c):
		s = s + tmp[j]
	s *= rep

	print 'Case #%d:' % (i + 1), process()
