f = open('A-large.in', 'r')
numCases = int(f.next())
for n in range(0, numCases):
	count = 0
	friends = 0
	line = map(None, f.next().split())
	shy_max = int(line[0])
	aud = map(int, list(line[1]))
	if aud[0] == 0:
		friends += 1
		count += 1
	else:
		count += aud[0]
	for i in range(1, len(aud)):
		if count < i:
			friends += i - count
			count += i - count + aud[i]
		else:
			count += aud[i]
	print "Case #" + str(n + 1) + ": " + str(friends)
