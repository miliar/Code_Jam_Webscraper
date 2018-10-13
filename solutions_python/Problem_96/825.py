#!/usr/bin/env python

import sys

def solvecase(N,S,p,T):
	count=0
	for ti in T:
		if ti%3==1:
			maxp=(ti-1)/3+1
			if maxp>=p:
				count+=1
		elif ti%3==2:
			maxp=(ti+1)/3
			if maxp>=p:
				count+=1
				continue
			else:
				maxp=(ti-2)/3+2
				if maxp>=p and S>0 and maxp<=10:
					count+=1
					S-=1
		else:  #ti%3==0
			maxp=ti/3
			if maxp>=p:
				count+=1
				continue
			else:
				maxp=ti/3+1
				if maxp>=p and S>0 and maxp<=10 and maxp-2>=0:
					count+=1
					S-=1
	return count

if __name__=="__main__":
	inpfile=open(sys.argv[1],'r')
	T=int(inpfile.readline())
	for i in range(0,T):
		inpline=inpfile.readline()
		inp=[int(x) for x in inpline.split()]
		ret=solvecase(inp[0],inp[1],inp[2],inp[3:3+inp[0]])
		print('Case #'+str(i+1)+': '+str(ret))
	inpfile.close()

