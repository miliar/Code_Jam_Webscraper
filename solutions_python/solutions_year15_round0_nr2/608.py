import sys

def solve(D, Ps):
	print D
	print Ps
	y = max(Ps)
	n = max(Ps)
	for i in range(2, n+1):
		m = i
		for P in Ps:
			m += P/i-1 if P%i==0 else P/i
		if m<y:
			y=m

	return y


def io(filename):
	output = open(filename.split('.')[0]+'.out', 'w')
	with open(filename, 'r') as f:
		T = int(f.readline())
		for t in range(T):
			D = int(f.readline())
			Ps = map(int, f.readline().split())
			output.write("Case #{x}: {y}\n".format(x=t+1, y=solve(D,Ps)))
			

if __name__ == '__main__':
	input_file = sys.argv[1]
	io(input_file)