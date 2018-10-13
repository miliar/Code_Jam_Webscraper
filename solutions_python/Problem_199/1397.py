t = input()

def change(char):
	return "+" if char == "-" else "-"

for case in xrange(t):
	line = raw_input().split(" ")
	row = list(line[0])
	k = int(line[1])
	can = True
	flips = 0
	for pos in xrange(len(row)):
		if row[pos] == "-":
			if pos + k > len(row):
				can = False
				break
			else:
				flips += 1
				for i in xrange(pos, pos + k):
					row[i] = "+" if row[i] == "-" else "-"
	print "Case #{}:".format(case + 1),
	print flips if can else "IMPOSSIBLE"

