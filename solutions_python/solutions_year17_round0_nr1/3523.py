def pancake(s, k):
	slen = len(s);
	count = 0
	sidx = 0
	slist = list(s)
	while sidx < slen:
		if (slist[sidx] == '-'):
			if (sidx + k <= slen):
				count += 1
				for j in range(k):
					if (slist[sidx + j] == '+'):
						slist[sidx + j] = '-'
					else:
						slist[sidx + j] = '+'
			else:
				return -1
		sidx += 1
	return count

t = int(raw_input().strip())
for a0 in range(t):
	line = raw_input().strip().split(' ')
	s = line[0]
	k = int(line[1])
	count = pancake(s, k)
	if count < 0:
		print("Case #" + str(a0 + 1) + ": IMPOSSIBLE")
	else:
		print("Case #" + str(a0 + 1) + ": " + str(count))