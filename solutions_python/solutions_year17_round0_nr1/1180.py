
def main():
	solutions = []
	with open('A-large.in', 'r') as f:
		rows = int(f.readline())
		for i in xrange(rows):
			tc = f.readline()
			S = list(tc.split(' ')[0])
			K = int(tc.split(' ')[1])
			S = [(0 if i=='-' else 1) for i in S]
			#print(K)
			#print(S)
			sol = solve(S, K)
			solutions.append("IMPOSSIBLE" if sol == -1 else sol)
			
	with open('A-large.out', 'w') as f:
		counter = 1
		for line in solutions:
			f.write("Case #{0}: {1}\n".format(str(counter), line))
			counter += 1

def solve(S, K):
	counter = 0
	for i in xrange(len(S) - K+1):
		if S[i] == 0:
			swap(S, i, K)
			counter += 1
	res = True
	for i in xrange(len(S) - K+1, len(S)):
		res = res and S[i]==1
	
	return counter if res else -1
	
def swap(S, i, K):
	for j in xrange(i, i+K):
		S[j] = 1 if S[j] == 0 else 0
		
main()
