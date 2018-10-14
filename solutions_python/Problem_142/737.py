#! /usr/bin/python

import sys
import math

def compute(M):
	li = len(M)
	lj = len(M[0])
	
	act = []

	for j in xrange(lj):
		col = map( lambda x: x[j], M )
		tmp = []
		for t in xrange(min(col), max(col)+1):
			for i in xrange(li):
				tmp.append( abs(M[i][j]-t) )
		act.append( max(tmp) )

	return sum(act)


def exec_test(n, S):

	let = []
	num = []
	nums = []

	let.append(S[0][0])
	count = 1

	for x in xrange( len(S[0]) ):
		if x==0:
			continue
		if( S[0][x]!=let[-1] ):
			let.append(S[0][x])
			num.append(count)
			count = 1
		else:
			count = count+1
	num.append(count);
	nums.append(num)

	loose=0

	for y in xrange( n ):
		if y==0:
			continue
		cur=0
		num = []
		count = 0
		for x in xrange( len(S[y]) ):
			if( S[y][x] != let[cur] ):
				if(x==0):
					loose=1
					break
				cur=cur+1
				if( cur==len(let)):
					losse=1
					break
				if( S[y][x] != let[cur] ):
					loose=1
					break
				else:
					num.append(count)
					count=1
			else:
				count = count+1
		if(cur!=len(let)-1 or loose==1):
			loose=1	
			break
		else:
			num.append(count)
		nums.append(num)

	print let
	print nums

	if loose==1:
		return " Fegla Won"

	res = compute( nums )

	return " %i" % res

# ====== READ INPUT ====================================

assert len(sys.argv)>=2, "Need input file"
input_file = sys.argv[1]
fd = open(input_file, 'r')
fd_out = open(input_file+".out", 'w')
n = int(fd.readline().split()[0]) # Number of tests
for test in xrange(n):
	print "=== Test #%i ===" % (test+1)
	num_str = int(fd.readline().split()[0])
	S = [];
	for i in xrange(num_str):
		S.append( fd.readline()[:-1] );
	ret = exec_test(num_str, S)
	strret = "Case #%i:%s" % ((test+1), str(ret))
	print strret
	fd_out.write(strret+"\n")

