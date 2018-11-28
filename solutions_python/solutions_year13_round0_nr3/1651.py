
def isPalindrome(n):
	num = str(n)
	return (num[::-1] == num)

	

def iter3(n):
	num = [0]
	val10 = reduce(lambda x,y: 10*x + y, num, 0)

	while len(num) < n:
		yield int(''.join([str(x) for x in num]), 10)
		num.reverse()
		i = 0
		while i < len(num):
			if num[i] < 2:
				num[i] += 1
				break
			else:
				num[i] = 0

			i += 1
		if i == len(num):
			num.append(1)
		
		num.reverse()
		
		
numbers = []
for x in iter3(14):
	if isPalindrome(x) and isPalindrome(x*x):
		numbers.append(x*x)
		#print "%d : %s" % (len(str(x*x)), x*x)


import sys
import bisect

bisect.insort(numbers, 9)

T = int(sys.stdin.readline(), 10)
for casenum in xrange(1,T+1):
	a,b = map(lambda x: int(x, 10), sys.stdin.readline().split(' '))
	ai = bisect.bisect_left(numbers, a)
	bi = bisect.bisect_right(numbers, b)

	print "Case #%d: %d" % (casenum, (bi-ai))

