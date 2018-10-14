import sys

lines =[]
for line in open(sys.argv[1]):
	line = line.strip()
	if " " in line:
		line = line.split(" ")
		line = map(int, line)
	else:
		line = int(line)
	lines.append(line)

for t in range(0, lines[0]):
	first = 10 * t + 1
	second = 10 * t + 6
	A = set(lines[lines[first] + first])
	B = set(lines[lines[second] + second])
	C = list(set(A).intersection(B))
	if len(C) == 1:
		print "Case #" + str(t + 1) + ": " + str(C[0])
	elif len(C) == 0:
		print "Case #" + str(t + 1) + ": Volunteer cheated!"
	elif len(C) > 1:
		print "Case #" + str(t + 1) + ": Bad magician!"
