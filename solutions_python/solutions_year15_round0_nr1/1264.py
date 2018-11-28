import sys

filepath = sys.argv[1]
outfile = sys.argv[2]

out = open(outfile, "w")
with open(filepath, "r") as f:
	trials = int(f.readline())
	for i in range(trials):
		extras = 0
		total = 0
		SMax, people = f.readline().split()
		SMax = int(SMax)

		for j, c in enumerate(people):
			S = int(c)
			if total < j:
				extras += 1
				total += 1
			total += S
		out.write("Case #{}: {}\n".format(i+1, extras))
