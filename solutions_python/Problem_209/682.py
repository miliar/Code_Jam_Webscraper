
import math
from decimal import *
max_s = 0
def recurse(start,n,cakes,acc):
	global max_s
	if n<=0:
		if acc > max_s:
			max_s = acc
	else:
		for i in range(start,len(cakes)):
			res = acc + 2*cakes[i]['r']*cakes[i]['h']
			#if res > max_s:
			#	max_s = res
			recurse(i+1,n-1,cakes,res)

t = int(raw_input())
for x in range(t):
	max_s = 0
	n,k = map(int,raw_input().split())
	cakes  = []
	for i in range(n):
		r,h = map(int,raw_input().split())
		cakes.append({'r':r,'h':h})

	cakes.sort(key=lambda x: x['r'],reverse=True)
	#print cakes
	for i in range(n-k+1):
		recurse(i+1,k-1,cakes,cakes[i]['r']**2 + 2*cakes[i]['r']*cakes[i]['h'])
	
	print "Case #{}:".format(str(x+1)),
	print "{0:0.9f}".format(max_s*(math.pi))
	