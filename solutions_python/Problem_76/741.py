#!/usr/bin/python

from scipy import *

def to_binary(x):
	result = zeros(20,dtype="int")

	for i in range(20):
		result[i] = x % 2
		x = x / 2
	return result

T = int(raw_input())
		
def check_equal(a,b):

	sum_a = sum(a,axis=0)
	sum_b = sum(b,axis=0)
	
	for i in range(20):
		if abs(sum_a[i] - sum_b[i]) % 2  != 0:
			return False
	return True

max_score = 0

def check_all(cand,binary_cand,depth,sean,patrick,l):
	global max_score
	if depth==len(cand)-1:
		if sum(cand[sean]) > max_score:
			if(check_equal(binary_cand[sean,:],binary_cand[patrick,:])):
				max_score = sum(cand[sean])
		return

	check_all(cand,binary_cand,depth+1,sean+[l[depth]],patrick,l)
	check_all(cand,binary_cand,depth+1,sean,patrick+[l[depth]],l)
			

for test_case in range(T):
	max_score = 0
	N = int(raw_input())
	line = raw_input()
	cand = array([int(con) for con in line.split(" ")])
	binary_cand = []

	for c in cand:
		binary_cand.append(to_binary(c))
	binary_cand = array(binary_cand)

	for i in range(len(cand)):
		tmp = range(len(cand))
		del tmp[i]
		check_all(cand,binary_cand,0,[],[i],tmp)

	if max_score == 0:
		print "Case #%d: NO" % (test_case+1)
	else:
		print "Case #%d: %d" % (test_case+1,max_score)
