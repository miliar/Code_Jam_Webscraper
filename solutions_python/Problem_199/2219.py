t = int(raw_input())  # read a line with a single integer
for j in xrange(1, t + 1):
  n, m = [str(s) for s in raw_input().split(" ")]
  s = list(str(n))
  k = int(m)
  changes = 0
  for i in range(0, len(s)):
  	if s[i] == '-' and i+k-1<len(s):
  		for i in range(i,i+k):
  			if s[i] == '+':
  				s[i] = '-'
  			elif s[i] == '-':
  				s[i] = '+'
  		changes = changes + 1
  count = True
  for thing in s:
  	if thing == '-':
  		count = False
  if count:
  	print "Case #{}: {}".format(j,changes)
  else:
  	print "Case #{}: IMPOSSIBLE".format(j)