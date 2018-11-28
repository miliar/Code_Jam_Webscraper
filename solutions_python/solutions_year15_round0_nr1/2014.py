def getNumFriends (smax, svals):
	if smax == 0:
		return 0
	num = int(svals[0])
	added = 0
	for i in range(1, smax + 1):
		if int(svals[i]) > 0 and i > num:
			added += i - num
			num = i
		num += int(svals[i])
	return added

n = int(raw_input())
for case in range(1, n + 1):
	line = raw_input().split()
	friends = getNumFriends(int(line[0]), line[1])
	print "Case #" + str(case) + ": " + str(friends)
