import sys

i = sys.stdin
n = int(i.readline())

for _n in xrange(1,n+1):
  N,l,h = map(int,i.readline().split())
  nums = map(int,i.readline().split())
  found = False
  for m in xrange(l,h+1):
    l = [True if ((m%p==0) or (p%m==0)) else False for p in nums]
    if False not in l:
      found = True
      break

  print "Case #%i:"%_n,
  if found:
    print "%i"%m
  else:
    print "NO"
