import sys

def readFile(filename):
	with open(filename, 'r') as fp:
		T = int(fp.readline())
		L = []
		for line in fp:
			line = line.strip().split(' ')
			L.append([int(l) for l in line])
		return T, L

def solve(n, k):
	if k==1:
		return n/2, (n-1)/2
	if n%2 == 1:
		return solve(n/2, k/2)
	else:
		if k%2==1:
			return solve(n/2-1, k/2)
		else:
			return solve(n/2, k/2)

if __name__ == "__main__":
	input_filename = sys.argv[1]
	T, L = readFile(input_filename)
	fp = open('output.txt', 'w')
	for i in range(T):
		ma, mi = solve(L[i][0], L[i][1])
		result = "Case #{}: {} {}".format(i+1, ma, mi)
		fp.write(result)
		if not i==T-1:
			fp.write('\n')
