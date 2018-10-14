#!/usr/local/bin/python

fin=file("B-large.in.txt")
fout=file("output.txt",'w')

casenum=int(fin.readline())

for n in range(0,casenum):
	C, F, X = fin.readline().split()
	C=float(C)
	F=float(F)
	X=float(X)

	cookie=0.0
	rate=2
	totaltime=0.0

	while (C/rate + X/(rate+F)) <= X/rate:
		totaltime+=C/rate
		rate+=F

	totaltime+=X/rate

	fout.write('Case #%d: %.7f\n' %(n+1,totaltime))


	