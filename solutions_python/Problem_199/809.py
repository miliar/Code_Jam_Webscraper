t = int(raw_input())  # read a line with a single integer
for counter in xrange(1, t + 1):
  s, k = [l for l in raw_input().split(" ")]
  s = list(s)
  k = int(k)
  n=0
  for i in range(len(s)):
    if s[i]=='+':
      continue
    else:
      if i>len(s)-k:
	n="IMPOSSIBLE"
      else:
        n=n+1
        for j in range(i, i+k):
         if(s[j]=='-'):
	   s[j]='+'
         else:
	   s[j]='-'
  print "Case #{}: {}".format(counter, n)
