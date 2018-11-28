import sys

def solve(line):
	div = str.split(line)
	max = int(div[0])
	if max == 0:
		return 0
	else:
		vals = div[1]
		sums = {}
		adds = 0
		sums[0] = 0
		for val in range(len(vals)-1):
			newsum = sums[val] + int(vals[val])
			sums[val+1] = newsum
			if newsum + adds < val + 1:
				adds = val + 1 - newsum
		return adds

def main(input):
	rFile = open(input, 'r')
	wFile = open('output.txt', 'w')
	exs = int(rFile.readline())
	for line in range(exs):
		sol = solve(rFile.readline())
		wFile.write('Case #' + str(line+1) + ': ' + str(sol) + '\n')
	rFile.close()
	wFile.close()

if __name__ == '__main__':
	main(sys.argv[1])