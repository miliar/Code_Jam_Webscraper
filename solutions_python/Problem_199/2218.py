t = int(raw_input())  # read a line with a single integer
for j in xrange(1, t + 1):
  n, m = [str(s) for s in raw_input().split(" ")]  
  #print "Case #{}: {} {}".format(i, n, m)
  s = list(str(n))
  k = int(m)
  numOfChanges = 0
  for i in range(0, len(s)):
  	if s[i] == '-' and i+k-1<len(s):
  		for i in range(i,i+k):
  			if s[i] == '+':
  				s[i] = '-'
  			elif s[i] == '-':
  				s[i] = '+'
  		numOfChanges = numOfChanges + 1
  flag = True
  for item in s:
  	if item == '-':
  		flag = False
  if flag:
  	print "Case #{}: {}".format(j,numOfChanges)
  else:
  	print "Case #{}: IMPOSSIBLE".format(j)