#!/usr/bin/env python
import sys

def getIntersect(ws):
	ws = ws[:]
	result = 0
	while(len(ws)>1):
		w = ws[0]
		for x in ws:
			if (w[0]>x[0] and w[1]<x[1]) or (w[0]<x[0] and w[1]>x[1]):
				result += 1
		ws.remove(w)	
	return result

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
        n = int(f.readline())
        w=[]
        for j in range(n):
            l = f.readline().split()
            a=int(l[0])
            b=int(l[1])
            w.append((a,b))
        inputs.append(w)
    return inputs
   
if __name__=='__main__':
    inputs = rf(sys.argv[-1])
    results = []
    for w in inputs:
        print w
        r = getIntersect(w)
        results.append(r)
    wf(sys.argv[-1][:-2]+'out',results)

