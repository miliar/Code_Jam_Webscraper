#!/usr/bin/env python
import sys
infile = sys.argv[1]
#outfile = sys.argv[2]

indata = open(infile, 'r').readlines()
#print indata

numcases = int(indata[0].strip())
lines = [x.strip().split(' ') for x in indata[1:]]

def solve(L, t, N, C, A):
	tp = t/2
	totaldistance = sum(A)*(N/C) + sum(A[0:(N%C)])
	if L == 0:
		return totaldistance*2
	Awithcount = []
	#calculate partial star (heading to)
	pstar = None
	numfull = tp / sum(A)
	rem = tp % sum(A)
	if rem == 0:
		pstar = numfull*C
		pstartimebenefit = 0
		timeforpstar = A[-1]*2
		normaltimeforpstar = A[-1]*2
		for i in range(0, C):
			Awithcount.append((A[i],N/C - numfull + (1 if i < N%C else 0)))
	else:
		for i in range(0, C+1):
			if numfull*sum(A) + sum(A[0:i]) >= tp and pstar == None:
				if i == 0:
					assert False
				pstar = numfull*C + i
				pstartimebenefit = numfull*sum(A) + sum(A[0:i]) - tp
				timeforpstar = A[i-1]*2 - pstartimebenefit
				normaltimeforpstar = A[i-1]*2
				for j in range(0, C):
					Awithcount.append((A[j],N/C - numfull + (1 if j < N%C else 0) - (1 if j < i else 0)))
	if pstar > N:
		pstar = None
	if pstar == None:
		return totaldistance*2
	#print pstar


	#Time before partial star
	time = 2*(  sum(A)*((pstar-1)/C) + sum(A[0:((pstar-1)%C)])  )
	#print time

	#print pstartimebenefit
	#print timeforpstar
	#print normaltimeforpstar
	Awithcount.sort(key=lambda x: -x[0])
	#print Awithcount

	pstarused = False
	for x in Awithcount:
		xbenefit = x[0]
		if pstartimebenefit > xbenefit and not pstarused and L>0:
			time += timeforpstar
			L -= 1
			pstarused = True
		if L > 0 and L>= x[1]:
			time += x[0]*x[1]
			L -= x[1]
		elif L>0 and L<x[1]:
			time += x[0]*L + 2*x[0]*(x[1]-L)
			L = 0
		else:
			time += 2*x[0]*x[1]
		#print x, time, L

	if L>0 and not pstarused:
			time += timeforpstar
			L -= 1
			pstarused = True
	elif not pstarused:
		time += normaltimeforpstar
		pstarused = True
	return time
			



	#if rem == 0:
	#	Awithcount = [(a,N/C - numfull) for a in A]
	#for a in A:
		

	#if L == 1:
		

for j in range(0, numcases):
	L = int(lines[j][0])
	t = int(lines[j][1])
	N = int(lines[j][2])
	C = int(lines[j][3])
	A = [int(x) for x in lines[j][4:]]
	assert(C == len(A))

	answer = solve(L, t, N, C, A)


	print "Case #" + str(j+1) + ": " + str(answer)
