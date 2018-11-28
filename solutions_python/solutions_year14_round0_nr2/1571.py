f = file('B-large.in')
g = file("output.txt", "w")
f.readline()
for n, line in enumerate(f):
	const = [float(x) for x in line.split()]
	rate = 2
	tCurr = const[2] / rate
	tNext = const[0] / rate + const[2] / (rate + const[1])
	total = 0
	while tCurr > tNext:
		total += const[0] / rate
		rate += const[1]
		tCurr = const[2] / rate
		tNext = const[0] / rate + const[2] / (rate + const[1])
	total += const[2] / rate
	g.write("Case #" + str(n + 1) + ": " + format(total, ".7f") + "\n")