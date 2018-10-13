def cal(timeAvail, fromPos, toPos):
	timeUse = abs(toPos - fromPos) - timeAvail
	if timeUse < 0:
		timeUse = 0
	return timeUse + 1


number_of_test_case = int(raw_input())
t = 1
while t <= number_of_test_case:
	line = raw_input().strip().split()
	posO = 1
	posB = 1
	timeAvailO = 0
	timeAvailB = 0
	ans = 0
	n = int(line[0])
	n_counter = 0
	base_pointer = 1
	while n_counter < n:
		if line[base_pointer] == 'O':
			timeUse = cal(timeAvailO, posO, int(line[base_pointer + 1]))
			timeAvailO = 0
			timeAvailB += timeUse
			posO = int(line[base_pointer + 1])
		else:
			timeUse = cal(timeAvailB, posB, int(line[base_pointer + 1]))
			timeAvailB = 0
			timeAvailO += timeUse
			posB = int(line[base_pointer + 1])
		ans += timeUse
		base_pointer += 2
		n_counter += 1
	print 'Case #%d: %d' % (t, ans,)
	t += 1
	
