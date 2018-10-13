inp = file("input")
T = inp.readline()
out = file("output", "w")
case = 0

for line in inp.readlines():
	case += 1
	line = line.split()
	C = int(line[0])
	D = int(line[1 + C])
	combine = {}
	oppose = {}
	for c in xrange(1,C+1):
		combine[line[c][0] + line[c][1]] = line[c][2]
		combine[line[c][1] + line[c][0]] = line[c][2]
	for d in xrange(2 + C, D + 2 + C):
		oppose[line[d][0]] = line[d][1]
		oppose[line[d][1]] = line[d][0]
	inv = line[-1]
	end = ''
	l = ''
	fl = ''
	for j in xrange(0,len(inv) + 1):
		if j < len(inv):
			l += inv[j]
		else:
			fl += l
		if len(l) > 1:
			if l in combine:
				l = combine[l]
		for letter in l:
			if letter in oppose:
				if oppose[letter] in fl + l:
					l = ''
					fl = ''
				break
		if len(l) == 2:
			fl += l[0]
			l = l[1]
	a = '['
	for i in xrange(len(fl)):
		a += fl[i]
		if i < len(fl) - 1:
			a += ', '
	a += ']\n'
	out.write("Case #" + str(case) + ": " + a)
