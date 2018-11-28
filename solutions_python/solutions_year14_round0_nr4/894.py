# -*- coding: utf-8 *-*
import ContestSolver as ContestSolver
import bisect


def compactify(N, K):
	if len(K) == 0:
		if len(N) == 0:
			return []
		else:
			return [[len(N), 0]]
	numN = bisect.bisect(N, K[0])
	#print numN
	if numN == len(N):
		threshold = 1
	else:
		threshold = N[numN]
	numK = bisect.bisect(K, threshold)
	#print numK
	return [[numN, numK]] + compactify(N[numN:], K[numK:])


def removezeros(data):
	return [x for x in data if x != [0,0]]


def recompactify(data):
	if len(data) == 0:
		return data
	data = removezeros(data)
	#print data
	for i in range(len(data)-1, 0, -1):
		if data[i][0] == 0:
			data[i-1][1] += data[i][1]
			data[i] = [0,0]
	#print data
	data = removezeros(data)
	#print data
	for i in range(0, len(data)-1):
		if data[i][1] == 0:
			data[i+1][0] += data[i][0]
			data[i] = [0,0]
	#print data
	data = removezeros(data)
	return data


def war(data):
	#print data
	if len(data) == 0:
		return 0
	if len(data) == 2 and data[0][0] == 0 and data[1][1] == 0:
		return data[0][1]
	data = [[v - min(x) for v in x] for x in data]
	#print data
	data = recompactify(data)
	return war(data)


def dwar(data):
	#print data
	if len(data) == 0:
		return 0
	if len(data) == 1:
		return data[0][0]
	flat = [x for sub in data for x in sub]
	data2 = [flat[i:i+2] for i in range(1, len(flat)-1, 2)]
	#print data2
	data2 = [[v - min(x) for v in x] for x in data2]
	#print data2
	flat2 = [flat[0]] + [x for sub in data2 for x in sub] + [flat[-1]]
	data = [flat2[i:i+2] for i in range(0, len(flat), 2)]
	#print data
	data = recompactify(data)
	return dwar(data)


def solver(case):
	N = sorted(case[1], key=lambda x: map(int, ("%.5f" % x).split(".")))
	K = sorted(case[2], key=lambda x: map(int, ("%.5f" % x).split(".")))
	data = compactify(N, K)
	return [int(case[0][0])-dwar(data), war(data)]

solution = ContestSolver.ContestSolver(solver, nosinglelists=False)
#solution.run("D-test", floats=True, test=True)
#solution.run("D-small-attempt0", floats=True)
solution.run("D-large", floats=True)

