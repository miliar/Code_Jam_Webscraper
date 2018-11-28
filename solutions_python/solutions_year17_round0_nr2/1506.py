n = int(raw_input().strip())
case_no = 0
while(n):
	n -= 1
	case_no += 1
	num = raw_input().strip()
	lnum = len(num)
	ind = 0
	for i in xrange(lnum-1):
		if (num[i] > num[i+1]):
			num = num[:i] + str(int(num[i]) - 1) + '9'*(lnum - i - 1)
			ind = i
			break
	ind -= 1
	while (ind >= 0):
		if (num[ind] > num[ind + 1]):
			num = num[:ind] + str(int(num[ind]) - 1) + '9' + num[ind+2:]
		else:
			break
		ind -= 1
	out = "Case #"+str(case_no) + ': ' + num.lstrip('0')
	print out