#!/usr/bin/env python

import fileinput

def prod(lst):
	product=1.0
	for x in lst:
		product *= x
	return product
	
def findsmall(passnums,probs):
	A=passnums[0]
	B=passnums[1]
	pcorrect=prod(probs)
	pwrong=1.0-pcorrect
	pcExpected=(B-A+1)*pcorrect +pwrong*(2*B-A+2)
	peExpected=B+2
	minnum=min((pcExpected,peExpected))
	pbExpected=0
	i=1
	while i < (B+1)/2 and pbExpected <= minnum:
		A=A-i
		pcorrect=prod(probs[:-i])
		pwrong=1.0-pcorrect
		pcExpected=(B-A+1)*pcorrect+pwrong*(2*B-A+2)
		pbExpected=1+pcExpected
		if pbExpected < minnum: minnum=pbExpected
	
	if pbExpected < minnum: minnum=pbExpected
	return minnum	
	
		
k=1
for line in fileinput.input():
	
	if fileinput.isfirstline():
		T=int(line) # no. of test cases
		continue
	if fileinput.lineno() % 2 ==0:
		nums=line.split()
		passnums=[int(x) for x in nums]		
	else:
		p=line.split()
		probs=[float(x) for x in p]
		prob=findsmall(passnums,probs)
		print "Case #%(k)i: %(prob)f" % {"k":k,"prob":prob}
		k +=1
	
