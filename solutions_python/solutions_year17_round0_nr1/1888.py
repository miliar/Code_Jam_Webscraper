import sys

t = int(raw_input())

for i in xrange(1, t+1):
  s, k = raw_input().strip().split()
  k = int(k)
  s = list(s)
  l = 0
  cnt = 0
  while l <= len(s)-k:
    if s[l] == "-":
      for j in xrange(k):
        if s[l+j] == '-':
          s[l+j] = '+'
        else:
          s[l+j] = '-' 
      cnt += 1        
    l += 1
  if '-' in s[-k:]:
    res = "IMPOSSIBLE"
  else:
    res = cnt


  print "Case #{}: {}".format(i, res)
