#MAM, Google Code Jam - Round1A, Problem A

def solveOne(line):

	answer = 0
	maxSlope = 0

	for i in xrange(len(line)-1):
		temp = max(0, line[i] - line[i + 1])
		answer += temp
		maxSlope = max(temp, maxSlope)

	return answer, maxSlope

def solveTwo(line, maxSlope):

	answer = 0

	for i in xrange(len(line)-1):
		answer += min(line[i], maxSlope)

	return answer

def solve(line):

	line = [int(i) for i in line.rstrip().split()]

	one, maxSlope = solveOne(line)
	two = solveTwo(line, maxSlope)

	answer = str(one) + " " + str(two)
	return answer

def main():
	with open('A-large.in', 'r') as infile, open('output.txt', 'w') as outfile:
		
		T = int(infile.readline())
		for x in xrange(T):
			N = infile.readline()
			line = infile.readline()
			outfile.write("Case #" + str(x + 1) + ": " + str(solve(line)) + "\n")

if __name__ == "__main__":
	main()