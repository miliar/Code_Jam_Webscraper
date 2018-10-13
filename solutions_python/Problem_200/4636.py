def is_tidy(num):
	if len(num) == 1:
		return True
	if all(int(num[i]) <= int(num[i+1]) for i in xrange(len(num)-1)):
		return True
	else:
		return False

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = raw_input()
  last_tidy = 1
  for k in reversed(xrange(1,int(n)+1)):
  	if is_tidy(str(k)):
		last_tidy = k
		break
  print "Case #{}: {}".format(i, last_tidy)
  # check out .format's specification for more formatting options
