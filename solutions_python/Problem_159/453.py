import sys

def solve(N,M):
	x=0
	diffs = []
	for i in range(N-1):
		diff = M[i] - M[i+1]
		diffs.append(diff)
		if diff>0:
			x+=diff
	y = 0
	y_rate = max(diffs)

	for m in M[:-1]:
		if m > y_rate:
			y+=y_rate
		else:
			y+=m

	return "{x} {y}".format(x=x,y=y)


def io(filename):
	output = open(filename.split('.')[0]+'.out', 'w')
	with open(filename, 'r') as f:
		T = int(f.readline())
		for t in range(T):
			N = int(f.readline())
			m = map(int,f.readline().split())
			output.write("Case #{n}: {xy}\n".format(n=t+1, xy=solve(N,m)))	

if __name__ == '__main__':
	input_file = sys.argv[1]
	io(input_file)