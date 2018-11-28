t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t+1):
	s, k = raw_input().split(" ")  # read a list of integers, 2 in this case
  	k = int(k)
  	ans = 0
  	char = list(s)
  	for j in xrange(len(char)):
		if char[j] == "-":
			if ((j+k) <= len(s)):
				ans += 1
				for x in xrange(k):
					if char[j+x] == "-":
						char[j+x] = "+"
					else:
						char[j+x] = "-"
			else:
				ans = "IMPOSSIBLE"


  	print "Case #{}: {}".format(i, ans)