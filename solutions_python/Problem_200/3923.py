def solve(numString):
	digits = list(numString)
	tidy = []
	for i in xrange(len(digits) - 1, 0, -1):
		if digits[i] == digits[i - 1]:
			if digits[i] == '0':
				digits[i - 1] = '9'
				tidy.append('9')
			else:
				tidy.append(digits[i])	
		elif digits[i] < digits[i - 1]:
			tidy.append('9')
			if digits[i - 1] == '0':
				digits[i - 1] = '9'
			else:
				digits[i - 1] = chr(ord(digits[i - 1]) - 1)
		else:
			tidy.append(digits[i])

	tidy.append(digits[0])
	tidy = tidy[::-1]
	tidyNumString = ''.join(tidy).lstrip('0')
	tidyNumList = list(tidyNumString)
	for i in xrange(len(tidyNumList) - 1):
		if tidyNumList[i + 1] < tidyNumList[i]:
			tidyNumList[i + 1] = tidyNumList[i]
	return ''.join(tidyNumList)

inFile = 'B-small-attempt0.in'
with open(inFile) as f:
    content = f.readlines()

content = [x.strip() for x in content]
nums = content[1:]

results = []
for n in nums:
	res = solve(n)
	results.append(res)

outFile = 'result'
with open(outFile, 'w') as f:
	for i in xrange(len(results)):
		line = 'Case #%d: %s\n' % (i + 1, results[i])
		f.write(line)
