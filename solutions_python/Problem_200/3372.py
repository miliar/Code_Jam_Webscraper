def tidy(n):
	if len(n)==1: return n
	for i in range(0, len(n)-1):
		if n[i] > n[i+1]:
			n[i] = n[i]-1
			n[i+1:] = [9]*(len(n)-i-1)
			n[:i+1] = tidy(n[:i+1])
			break
	return n

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n = int(raw_input())
	n = tidy([int(d) for d in str(n)])
	res = 0
	for d in n:
		res *= 10
		res += d
	print "Case #{}: {}".format(i, res)