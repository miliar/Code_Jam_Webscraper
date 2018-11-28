def check(s, n):
	acc = 0
	for index in range(len(s)):
		if s[index] == '-':
			#print "hello world"
			acc+=1
			s, acc = flip(s, int(n), index, acc)
			#print "acc is: " + str(acc)
			if acc == 0:
				return 'IMPOSSIBLE'
	return acc

def flip(s, n, index, acc):
	a = ""
	#print "length of s is: " + str(len(s)) + ", and n is: " + str(n) + " and index is: " + str(index)
	if len(s) >= n + index:
		for i in range(n):
			if s[index + i] == '+':
				a+='-'
			else:
				a+='+'
		#print a
		s = s[:index] + a + s[index+n:]
	else:
		#print "comes here"
		acc = 0
	#print "acc in flip is" + str(acc)
	#print s
	return s, acc

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, m = [str(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  ans = check(n, m)
  print "Case #{}: {}".format(i, ans)
  # check out .format's specification for more formatting options

