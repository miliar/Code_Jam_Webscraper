def isMonotone(num):
	prev = 0
	for c in str(num):
		if int(c) < prev:
			return False
		prev = int(c)
	return True

def decrement(char):
	v = int(char) - 1
	if v == -1:
		return '9'
	else:
		return str(v)

def adjustNumber(rawNumber):
	num = str(rawNumber)
	newNum = ''
	for i in range(len(num) - 1):
		c0 = num[i]
		c1 = num[i+1]

		if c1 >= c0:
			newNum += c0
		else:
			c0p = decrement(c0)
			padding =  '9' * (len(str(num)) - len(newNum + c0p))
			newNum = newNum + c0p + padding
			return adjustNumber(newNum)
	return int(newNum + c1)

N = int(raw_input())
for i in range(N):
	t = int(raw_input())
	if isMonotone(t) is False:
		t = adjustNumber(t)

	if isMonotone(t) is False:
		print 'ERROR %d -> %d' % (i+1, t)

	print 'Case #%d: %d' % (i+1, t)



