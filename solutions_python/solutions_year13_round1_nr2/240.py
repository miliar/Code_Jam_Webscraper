import math, multiprocessing

def getGain(par):
	E, R, N, value = par

	memo = [-1 for x in range(E+1)]
	prevMemo = [-1 for x in range(E+1)]

	# last activity
	for i in range(E+1):
		memo[i] = value[-1] * i
	
	for step in range(N-2, -1, -1):
		for e in range(E+1):
			currMax = 0
			for consume in range(e, -1, -1):
				next = e - consume + R
				if next > E:
					next = E
				thisGain = consume * value[step] + memo[next]
				if thisGain > currMax:
					currMax = thisGain
			prevMemo[e] = currMax
		temp = prevMemo
		prevMemo = memo
		memo = temp

	return memo[E]




if __name__ == '__main__':
	fIn = open('B-small-attempt0.in')
	fOut = open('output.txt', 'w')
	numOfTests = int(fIn.readline())

	data = []
	for t in range(numOfTests):
		E, R, N = [int(x) for x in fIn.readline().split()]
		value = [int(x) for x in fIn.readline().split()]
		data.append((E, R, N, value))
	
	#print(getGain(data[0]))	
	
	p = multiprocessing.Pool(4)
	results = p.map(getGain, data)
	
	for t in range(len(results)):
		fOut.write("Case #%d: %d \n" % (t+1, results[t]))
