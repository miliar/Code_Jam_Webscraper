def analyse(pc, k):
	answer = 0
	for i in range(len(pc)-k+1):
		if pc[i] == "-":
			pc = pc[:i] + pc[i:i+k].replace("+","x").replace("-","+").replace("x","-") + pc[i+k:]
			answer += 1
		#print(pc, answer)

	if "-" in pc:
		return "IMPOSSIBLE"
	else:
		return str(answer)


def run(name):
	lines = [l for l in open(name + ".in", mode='r')]
	n = int(lines[0])
	
	out = open(name + ".out",mode='w')
	for i, line in enumerate(lines[1:]):
		parts = line[:-1].split(" ")
		#print(parts)
		answer = analyse(parts[0], int(parts[1]))
		out.write("Case #" + str(i+1) + ": " + answer + "\n")
	out.close()

run("A-large")