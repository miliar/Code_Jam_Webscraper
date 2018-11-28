import math

def palindrome(t):
	if t%10 == 0:
		return False
	n = str(t)
	r = n[::-1]
	if n == r:
		return True
	return False


input_text = [line.strip() for line in open('input.txt')]
CASE_COUNT = int(input_text[0])
for CASE_NUM in range(1,CASE_COUNT+1):
	nums = input_text[CASE_NUM].split(" ")
	s1 = long(nums[0])
	e1 = long(nums[1])

	s = long(math.floor(math.sqrt(s1)))
	e = long(math.ceil(math.sqrt(e1)))

	cnt = 0
	for i in (x for x in xrange(s,e+1) if palindrome(x)):
		tmp = i**2
		if tmp >= s1 and tmp <= e1 and tmp%10 != 0:
			if palindrome(tmp):
				cnt +=1


	print "Case #%d: %s" % (CASE_NUM,cnt)