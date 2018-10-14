def solve(s, k):
	n = len(s)
	s = map(lambda c: 0 if c=='-' else 1, s)
	f = [0]*(n-k+1)
	f[0] = (1 + s[0] )% 2
	for i in range(1, n-k+1):
		l = max(i - k + 1, 0)
		f_sum = reduce(lambda x,y: x+y, f[l:i], 0) % 2
		f[i] = (s[i] + f_sum + 1) % 2
	# check impossibility
	for i in range(n-k+1, n):
		l = max(i - k + 1, 0)
		f_sum = reduce(lambda x,y: x+y, f[l:n], 0) % 2
		if (s[i] + f_sum) % 2 != 1:
			return -1
	return sum(f)

if __name__=='__main__':
	t = int(raw_input())
	for turn in range(t):
		line = raw_input()
		s, k = line.split(" ")
		k = int(k)
		num = solve(s, k)
		print "Case #"+str(turn+1)+":",
		if num != -1:
			print str(num)
		else:
			print "IMPOSSIBLE"
