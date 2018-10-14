def analyse(d, pancakes):
	bestCost = max(pancakes)
	for target in range(1, max(pancakes)):
		splittingCost = 0
		for size in pancakes:
			if size > target:
				splittingCost += int(size/target) - (1 if size % target == 0 else 0)
		cost = target + splittingCost
		if cost < bestCost:
			bestCost = cost

	return str(bestCost)

def run(name):
	lines = [l for l in open(name + ".in", mode='r')]
	n = int(lines[0])
	
	out = open(name + ".out",mode='w')
	for i in range(n):
		d = int(lines[2*i+1])
		pancakes = [int(p) for p in lines[2*i+2].split(" ")]
		answer = analyse(d,pancakes)
		out.write("Case #" + str(i+1) + ": " + answer + "\n")
		if "test" in name:
			print("Case #" + str(i+1) + ": " + answer)
	out.close()

run("B-large")