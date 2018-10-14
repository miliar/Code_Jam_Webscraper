#!/usr/bin/python3

import sys
import collections


def doSolve( N, K ):
	partlist = {}
	partlist[N] = 1
	
	# size of partlist never exceeds 4 or so
	# so I use whatever DS I want
	# Too lazy, hehe
	
	while True:
		od = collections.OrderedDict(sorted(partlist.items()))
		curEmpty, curCnt = od.popitem()
		del partlist[curEmpty]
		
		rstall = curEmpty-1
		ls = rstall//2
		rs = rstall-ls
		
		if ls in partlist:
			partlist[ls] = partlist[ls] + curCnt
		else:
			partlist[ls] = curCnt
		
		if rs in partlist:
			partlist[rs] = partlist[rs] + curCnt
		else:
			partlist[rs] = curCnt
		
		#print('ce=%d, cc=%d, rs=%d, ls=%d'%(curEmpty,curCnt,rs,ls))
		#print(collections.OrderedDict(sorted(partlist.items(),reverse=True)))
		if K > curCnt:
			K = K - curCnt
		else:
			return ls, rs
		


inputbuff = ''
def clearInputWhiteSpace():
	global inputbuff
	while True:
		if len(inputbuff) == 0:
			break
		if not (inputbuff[0] == ' ' or inputbuff[0] == '\n' or inputbuff[0] == ' '):
			break
		
		inputbuff = inputbuff[1:]

def readint():
	global inputbuff
	while True:
		clearInputWhiteSpace();
		inputbuff = inputbuff.replace('\n', ' ')
		inputbuff = inputbuff.replace('\r', ' ')
		clearInputWhiteSpace();
		
		csp = inputbuff.split(' ')
		if len(csp) < 2:
			inputbuff = inputbuff + sys.stdin.readline()
			continue
		else:
			inputbuff = ' '.join(csp[1:])
#			print('Got %d'%int(csp[0]))
			return int(csp[0])

def solveOne(case_num):
	n = readint()
	k = readint()
	
	ls, rs = doSolve(n, k)
	print('Case #%d: %d %d'%(case_num, rs, ls))


def mainfunc():
	casecnt = readint()
	for i in range(casecnt):
		res = solveOne(i+1)

mainfunc()

