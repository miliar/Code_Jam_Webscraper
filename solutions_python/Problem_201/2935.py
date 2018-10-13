
def ans(brs, no):
	maxi = brs
	a = [maxi]
	for i in xrange(1, no + 1):
		tos = max(a)
		a.remove(tos)
		tos = tos - 1
		if tos % 2 == 0:
			maxi = mini = tos / 2
			a.append(maxi)
			a.append(maxi)
		else:
			mini = max(tos / 2, 0)
			maxi = mini + 1
			a.append(maxi)
			a.append(mini)
	return (mini, maxi)


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  mini , maxi = ans(n, m)
  print "Case #{}: {} {}".format(i, maxi, mini)
  # check out .format's specification for more formatting options