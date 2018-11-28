def parse_line(file):
        line = []
        line = file.readline()
        line = line.split()
        line = [int(t) for t in line]
        return line

#f = open('./ex.txt', 'r')
f = open('./A-small-attempt0.in', 'r')
f_results = open('./result.txt', 'w')

cases = int(f.readline())

for case in range(cases):
        tt = list(parse_line(f))
        r = tt[0]
        t = tt[1]

	found = False
	ml = 0
	i = 1

	while not found:
		ml = 2 * r + 4 * i - 3
		if ml <= t:
			t -= ml
			i += 1
		else:
			found = True

	f_results.write("Case #" + str(case + 1) + ": " + str(i - 1) + "\n")
