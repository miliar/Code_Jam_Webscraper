fin = open("A-small-attempt0.in","r")
lines = fin.readlines()
n = 0
T = int(lines[n])
n += 1
for i in range(T):
	r1 = int(lines[n])-1
	n += 1
	a1 = []
	for j in range(4):
		tokens = lines[n].split(" ")
		n += 1
		a1.append(set([int(c) for c in tokens]))
	r2 = int(lines[n])-1
	n += 1
	a2 = []
	for j in range(4):
		tokens = lines[n].split(" ")
		n += 1
		a2.append(set([int(c) for c in tokens]))
	res = a1[r1].intersection(a2[r2])
	if len(res) == 0:
		print "Case #" + str(i+1) + ": Volunteer cheated!"
	elif len(res) == 1:
		print "Case #" + str(i+1) + ": " + str(list(res)[0])
	else:
		print "Case #" + str(i+1) + ": Bad magician!"
	