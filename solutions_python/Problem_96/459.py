#!/usr/bin/env python
#encoding=utf-8

'''
author:		Eric Zhang(snow31450588@gmail.com)
date:		2012-04-14
purpose:	Google Code Jam Qualification Round
history:
	2012-04-14	Initial version
'''

import sys
import string

def precal():
	dSurprising = {}
	dNonSurprising = {}
	dNonSurprising[0]=0
	dNonSurprising[1]=1
	for i in range(2,31):
		if i%3==0:
			dNonSurprising[i]=i/3
			dSurprising[i]=i/3+1
		elif i%3==1:
			dNonSurprising[i]=i/3+1
			dSurprising[i]=i/3+1
		elif i%3==2:
			dNonSurprising[i]=i/3+1
			dSurprising[i]=i/3+2
	return dNonSurprising, dSurprising

def calculate(l, dNonSurprising, dSurprising):
	ns = l.split()
	N = int(ns[0])
	S = int(ns[1])
	p = int(ns[2])
	ns = [int(n) for n in ns[3:]]
	ns.sort()
	ns.reverse()
	count = 0
	for n in ns:
		nonSurprising = dNonSurprising.get(n,0)
		surprising = dSurprising.get(n,0)
		if nonSurprising>=p:
			count += 1
			continue
		elif surprising>=p and S>0:
			count += 1
			S -= 1
			continue
		else:
			return count
	return count
    
def wf(fileName,results):
    f = open(fileName,'w')
    for i,r in enumerate(results):
        f.write('Case #%d: %s\n'%(i+1,r))
    f.close()

def rf(fileName):
    f = open(fileName,'r')
    inputs = []
    n = int(f.readline())
    for i in range(n):
        l = f.readline().strip()
        inputs.append(l)
    return inputs

def main(fin, fout):
    dNonSurprising, dSurprising = precal()
    inputs = rf(fin)
    
    results = []
    for l in inputs:
        e = calculate(l, dNonSurprising, dSurprising)
        results.append(e)
    wf(fout,results)


if __name__=='__main__':
	fin = sys.argv[1]
	fout = sys.argv[1][:-2]+'out'
	main(fin, fout)
