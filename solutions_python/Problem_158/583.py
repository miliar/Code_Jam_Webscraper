#MAM, Google Code Jam - Qualification Round, Problem 4

def toText(winnable):
	if winnable:
		return "GABRIEL"
	return "RICHARD"

def solve(line):

	X, R, C = [int(i) for i in line.rstrip().split(" ")]

	if (R * C) % X > 0:
		return toText(0)

	if X < 3:
		return toText(1)

	if X < 4:
		if (R > 1) and (C > 1):
			return toText(1)

	if (R > 2) and (C > 2):
		return toText(1)

	return toText(0)

def main():
	with open('D-small-attempt2.in', 'r') as infile, open('output.txt', 'w') as outfile:
		
		T = int(infile.readline())
		for x in xrange(T):
			line = infile.readline()
			outfile.write("Case #" + str(x + 1) + ": " + str(solve(line)) + "\n")

if __name__ == "__main__":
	main()