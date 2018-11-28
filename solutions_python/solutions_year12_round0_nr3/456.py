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


def calculate(l):
	count = 0
	A, B = l.split()
	a = int(A)
	b = int(B)
	for n in range(a,b):
		N = str(n)
		ls = []
		for i in range(1,len(N)):
			newN = int(N[i:]+N[:i])
			if newN>n and newN<=b:
				ls.append(newN)
		count += len(set(ls))
	return count

    
def wf(fileName,results):
    f = open(fileName,'w')
    for i,r in enumerate(results):
        f.write('Case #%d: %d\n'%(i+1,r))
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
    inputs = rf(fin)
    
    results = []
    for l in inputs:
        e = calculate(l)
        results.append(e)
    wf(fout,results)


if __name__=='__main__':
	fin = sys.argv[1]
	fout = sys.argv[1][:-2]+'out'
	main(fin, fout)
