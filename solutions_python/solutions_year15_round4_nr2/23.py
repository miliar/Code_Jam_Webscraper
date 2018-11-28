import math
import re
from decimal import *

def solve(n,v,x,taps):
	print n
	d = {}
	minc = 100.0
	maxc = 0.0
	for [r,c] in taps:
		minc = min(minc,c)
		maxc = max(maxc,c)
		if c in d.keys():
			d[c]+=r
		else:
			d[c]=r
	if minc>x or maxc<x:
		return -1
	vtot = 0
	vxtot = 0
	for c in d.keys():
		vtot += d[c]
		vxtot += c * d[c]
	print vtot, vxtot, vxtot-x*vtot
	l = sorted(d.keys())
	if vxtot/vtot>x:
		l = l[::-1]
	print l
	while vxtot/vtot!=x:
		vxnew = vxtot - l[0]*d[l[0]]
		vnew = vtot - d[l[0]]
		print vnew, vxnew, vxnew-x*vnew
		if (vxnew-x*vnew)/(vxtot-x*vtot)>0:
			vxtot = vxnew
			vtot = vnew
			l = l[1:]
		else:
			print "done"
			p = (x*vnew-vxnew)/(vxtot-vxnew-x*vtot+x*vnew)
			vxtot = p*vxtot+(1-p)*vxnew
			vtot = p*vtot + (1-p)*vnew
			print vtot, vxtot, vxtot-x*vtot
			break
	return v/vtot


def formatting(ans):
	print ans
	if ans==-1:
		return "IMPOSSIBLE"
	else:
		return str(ans)

inp = open("B-large.in","r")
out = open("B-large","w")
lines = inp.readlines()
i=1
count=1
while i<len(lines):
	[n,v,x] = [Decimal(y) for y in re.split(" ",lines[i])]
	n = int(n)
	taps = [[Decimal(y) for y in re.split(" ",lines[i+j])] for j in range(1,n+1)]
	out.write("Case #"+str(count)+": "+formatting(solve(n,v,x,taps))+"\n")
	i+=(n+1)
	count+=1
out.close()
inp.close()

