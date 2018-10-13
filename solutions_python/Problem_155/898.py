def solve(m,s):
	stoodCount = 0
	requireFriends = 0
	for i in range(0,len(s)):
		shyness = ord(s[i]) - ord('0')
		if shyness == 0:
			continue
		if i != 0 and i > stoodCount:
			requireFriends += (i - stoodCount)
			stoodCount = i
		stoodCount += shyness
	return requireFriends
t = input()
case = 1
while t:
	t -= 1
	line = raw_input().split()
	print "Case #%d: %d" % (case, solve(int(line[0]),line[1]))
	case += 1