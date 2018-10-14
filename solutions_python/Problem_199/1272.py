import fileinput
counter = 0
for line in fileinput.input():
	if not fileinput.isfirstline():
		s, k = line.split(' ')
		k = int(k)
		move = 0
		s = [ x == '+' for x in s ]
		for i in range(len(s)-k+1):
			if not s[i]:
				move += 1
				for j in range(k):
					s[i+j] = 1 - s[i+j]
		counter += 1
		if all(s):
			print("Case #%d: %d" % (counter, move))
		else:
			print("Case #%d: IMPOSSIBLE"% (counter))
