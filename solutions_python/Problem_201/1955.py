import sys
import bisect

t = int(raw_input())

for i in xrange(1, t+1):
  n, k = map(int, raw_input().strip().split())
  s = [n]
  for j in xrange(k):
    num = s.pop()
    if num % 2 != 0:
      ls = num/2
      lr = num/2
      if ls != 0:
        bisect.insort_left(s,ls)
        bisect.insort_left(s,lr)
    else:
      ls = num/2 -1
      lr = num/2
      if ls != 0:
        bisect.insort_left(s,ls)
        bisect.insort_left(s,lr)
      else:
        bisect.insort_left(s,lr) 
      
  print "Case #{}: {} {}".format(i, lr, ls)
