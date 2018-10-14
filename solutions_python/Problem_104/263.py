#!/usr/bin/python

import sys

inname = "input.txt"
outname = "output.txt"
if len(sys.argv)>1:
	inname = sys.argv[1]
	outname = inname.rstrip(".in")
	outname = outname + ".out"
fin = open(inname,"r")
fout = open(outname,"w")

def solveN(N,num):
#	num.sort()
#	T = [0,num[0],num[1],num[0]+num[1]]
#	S = [[],[0],[1],[1,2]]
	T = [0,num[0]]
	S = [[],[0]]
	flag = 0
	r0 = []
	r1 = []
	for i in range(1,N):
		M = len(T)
		for j in range(M):
			nt = num[i]+T[j]
			if nt not in T:
				T.append(nt)
				st = list(S[j])
				st.append(i)
			#	print "st:",st
				S.append(st)
			else:
				r1 = list(S[j])
				r1.append(i)
				r0 = S[T.index(nt)]
				flag = 1
				break
		if flag == 1:
			break
	res = ""
	if flag==0:
		res = "Impossible\n" 
	else:
	#	print r0
	#	print r1
		for v in r0:
			res += str(num[v]) + " "
		res += "\n"
		for v in r1:
			res += str(num[v]) + " "
		res += "\n"
	return res


line = fin.readline().rstrip("\n")
testCaseNum = int(line)
for caseNum in range(testCaseNum):
	data = [int(v) for v in fin.readline().rstrip("\n").split()]
	N = data[0]
	num = data[1:]
	res = solveN(N,num)
	print "case #%d\n" %(caseNum+1)
	answer = "Case #%d:\n" %(caseNum+1)
	answer += res
	fout.write(answer)

fin.close()
fout.close()
