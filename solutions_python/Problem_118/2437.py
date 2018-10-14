import math
def isPalindrome (num):
	i = 0
	j = len(num)-1
	result = True
	while (i < j):
		if (num[i] != num[j]):
			result = False
		i = i + 1
		j = j - 1
	return result
T = int(raw_input().strip())
#print T

for i in xrange(T):
	print 'Case #%s:' %(i+1),
	(start, end) = raw_input().strip().split()
	(numStart, numEnd) = (int(start), int(end))
	num = numStart
	sqrtStart = int(math.ceil(numStart**(1/2.0)))

	count = 0
	while (sqrtStart * sqrtStart) <= numEnd:
		if (isPalindrome(str(sqrtStart))):
			num = sqrtStart * sqrtStart
			if (isPalindrome(str(num))):
				count = count + 1
		sqrtStart = sqrtStart + 1
		#print strNum, isPalindrome(strNum)
	print count

	
