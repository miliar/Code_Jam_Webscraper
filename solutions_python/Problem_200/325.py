import sys
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
ints = []
for i in xrange(1, t + 1):
	n = raw_input()  # read a list of integers, 2 in this case
	ints.append(int(n))
	# print "Case #{}: {} {}".format(i, n + m, n * m)
	# check out .format's specification for more formatting options

	
def tidy(n):
	cur = 0
	s = str(n)
	for ele in s:
		if cur > int(ele):
			return False
		cur = int(ele)
	return True
		

def sol(n):
	if tidy(n):
		return str(n)
	if n < 10:
		return str(n)
	first = ''
	second = '' 
	s = str(n)
	curr = 0
	
	flag = 0
	for i in xrange(len(s)):
		if flag:
			second = second + '9'
		else:
			
			if curr > int(s[i]):
				flag = 1
				second = '9'
			else:
				first = first + s[i]
			curr = int(s[i])
	
	return sol(int(first)-1) + second
	

def sol2(n):
	return int(sol(n))


	
	
	
for i in xrange(t):
	res = sol(sol2(ints[i]))
	print "Case #{}: {}".format(i+1, res )
#   print "Case #{}: {} {}".format(i, n + m, n * m)

# for i in xrange(t):
	# print "Case #{}: {} ".format(i+1, sol(ints[i]) )