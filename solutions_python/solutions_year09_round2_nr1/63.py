#!/usr/bin/python
import sys
from types import *

def nextLine():
	return sys.stdin.next()[:-1]

def debug(s):
	sys.stderr.write("# "+s+"\n")

def readTree(str, p= 0):
	head = ""
	subs = []
	p = p+1
	while p < len(str):
		if str[p] == '(':
			subTree,pos = readTree(str,p)
			p = pos
			subs.append(subTree)
		elif str[p] == ')':
			head = head.split()
			head[0] = float(head[0])
			if len(subs) == 0:
				return head[0],p+1
			return (head[0],head[1],subs[0],subs[1]),p+1
		else:
			head += str[p]
			p+=1
			
def readAnimal(str):
	a = str.split()
	return a[2:]

def test(tree, bicho):
	p = 1.0
	if type(tree) is FloatType:
		p = p*tree
	else:
		H,T,S1,S2 = tree
		p = p*H
		if T in bicho:
			p = p*test(S1,bicho)
		else:
			p = p*test(S2,bicho)
	return p

N = int(nextLine())
for c in range(N):
	l = int(nextLine())
	str = ""
	for i in xrange(l):
		str += nextLine()
	
	t = readTree(str)[0]
	print "Case #%d:"%(c+1)
	l = int(nextLine())
	for i in xrange(l):
		bicho = readAnimal(nextLine())
		result = test(t,bicho)
		print "%.7f"%(result)

