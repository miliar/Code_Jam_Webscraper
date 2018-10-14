def analyse(inp):

	s = 0
	i = 0
	answer = ""

	for i in range(len(inp)-1):

		c = int(inp[i])
		n = int(inp[i+1])

		#print(str(i) + " " + str(c) + " " + str(n))
		if c < n:
			s = i+1
			i = i+1
		elif c == n:
			i = i+1
		elif c > n:
			#print(s, c, inp[:s], str(c - 1), len(inp), len(inp)-s-1)
			return str(int(inp[:s] + str(c - 1) + "9"*(len(inp)-s-1)))

	return inp


def run(name):
	lines = [l for l in open(name + ".in", mode='r')]
	n = int(lines[0])
	
	out = open(name + ".out",mode='w')
	for i, line in enumerate(lines[1:]):
		#print("Q" + str(i+1))
		answer = analyse(line[:-1])
		out.write("Case #" + str(i+1) + ": " + answer + "\n")
	out.close()

run("B-large")