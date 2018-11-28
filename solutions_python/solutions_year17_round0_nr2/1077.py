def tnum(k):
	res = [k[len(k)-1]]
	for i in xrange(len(k)-2, -1, -1):
		if k[i] == '0':
			res = ['9'] * len(res)
		elif int(k[i]) > int(k[i+1]):
			res = ['9'] * len(res)
			k[i] = str(int(k[i])-1)
		res = [k[i]] + res
	if res[0] == '0':
		res = res[1:]
	return ''.join(res)


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  k = raw_input()
  result = tnum(list(str(k)))
  print "Case #{}: {}".format(i, result)
  # check out .format's specification for more formatting options

