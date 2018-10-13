fileName = 'C-small-2-attempt0'

def main():
	solutions = []
	with open(fileName+'.in', 'r') as f:
		rows = int(f.readline())
		for i in xrange(rows):
			tc = f.readline()
			N = int(tc.split(' ')[0])
			K = int(tc.split(' ')[1])
			#print("+++*")
			#print(N)
			sol = solve(N, K)
			#print(sol)
			solutions.append(str(sol[0]) + ' ' + str(sol[1]))
			
	with open(fileName+'.out', 'w') as f:
		counter = 1
		for line in solutions:
			f.write("Case #{0}: {1}\n".format(str(counter), line))
			counter += 1

def solve(N, K):
	if K == 1:
		return (max(int(round(float(N - 1)/2)) , (N-1)/2), min(int(round(float(N - 1)/2)) , (N-1)/2))
	N = N - 1
	K = K - 1
	newN = int(round(float(N)/2))
	newK = int(round(float(K)/2))
	if K>1:
		return getWorst(solve(newN, newK), solve(N - newN, K - newK))
	else:
		return solve(newN, newK)

def getWorst(a, b):
	if a[0] < b[0]:
		return a
	elif a[0] > b[0]:
		return b
	elif a[1] < b[1]:
		return a
	else:
		return b

main()

