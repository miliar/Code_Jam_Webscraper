#!/usr/bin/python

import sys

def readFile(dir):
	f=open(dir)
	lines=f.readlines()
	T=int(lines[0])
	quizs=[l.split() for l in lines[1:]]
	return quizs


def f(n,F):
	return 2.0+F*n

def t(n,C,F,X):
	if n==0:
		return X/2.0
	t=0.0
	i=0
	while i<n:
		t+=C/f(i,F)
		i+=1
	t+=X/f(i,F)
	return t

def findMin(C,F,X):
	if X<=C:
		return t(0,C,F,X)
	t0=t(0,C,F,X)
	gap=50
	if X/(F*C)>50:
		gap=600
	p=gap
	while 1:
		t1=t(p,C,F,X)
		if t1<t0:
			t0=t1
			p+=gap
		else:
			return findMin1(p,C,F,X)

def findMin1(e,C,F,X):
	t0=t(e,C,F,X)
	p=e-1
	while p>0:
		t1=t(p,C,F,X)
		if t1<t0:
			t0=t1
			p-=1
		else:
			return t0
	return min(t0,t(0,C,F,X))



def findMin2(C,F,X):
	if X<=C:
		return t(0,C,F,X)
	t0=t(0,C,F,X)
	print t0
	p=1
	while p<2:
		t1=t(p,C,F,X)
		print t1
		p+=1


if __name__=="__main__":
	quizs=readFile(sys.argv[1])
	for i in range(len(quizs)):
		print ("Case #%s: %s" % (i+1,findMin(float(quizs[i][0]),float(quizs[i][1]),float(quizs[i][2]))))

