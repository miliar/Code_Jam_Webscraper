fh = open('out-a.txt', 'w')
with open('A-small-attempt2.in', 'r') as fp:
	T = int(fp.readline())
	for i in range(T):
		line = fp.readline().strip()
		line = list(line)
		line.remove(' ')
		line = list(map(int, line))
		maxShyness, line = (line[0], line[1:])
		if len(line) == 1:
			howMany = 0
		elif 0 not in line:
			howMany = 0
		else:
			times = line.count(0)
			howMany = 0
			lin = line
			tmp = 0
			for j in range(times):
				ind = lin.index(0)
				if ind == 0:
					howMany += 1
					lin[ind] = 1
					continue
				else:
					if sum(lin[:ind]) + tmp < ind+1:
						lin[ind] = 1
						howMany += 1
					else:
						lin[ind] = -1
						tmp += 1

		fh.write("Case #" + str(i+1) + ": " + str(howMany) + "\n")
fh.close()