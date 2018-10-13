with open("A-large.in") as f:
    lines = f.readlines()

numLines = int(lines[0])

for i in xrange(numLines):
	tmp = lines[i+1].strip().split(' ', 1)
	sMax = int(tmp[0]) + 1
	v = tmp[1]
	other = 0
	friend = 0
	j = 0
	while j < sMax:
		if int(v[j]) > 0:
			if j <= other + friend:
				other = other + int(v[j])
				j = j + 1
			else:
				friend = friend + 1
		else:
			j = j + 1

	print "Case #" + str(i+1) + ": " + str(friend)
