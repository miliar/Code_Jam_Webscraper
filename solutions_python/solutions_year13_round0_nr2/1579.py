def f(a):
  b=zip(*a) # transpose
  R=[sum(e) for e in a] # sum of rows
  C=[sum(e) for e in b] # sum of cols
  ok=0
  # one of rows/cols is different height, but others're the same height
  if (len(set(R))==2 and 0 in R) or (len(set(C))==2 and 0 in C): ok=1
  # all of lawns're the same height
  elif len(set(R))==1 and len(set(C))==1: ok=1

  really=0
  # if sum of array of arrays is 2, these should be the same line
  if sum(e for sublist in a for e in sublist)!=2 or 2 in R or 2 in C: really=1
  return ok and really

for case in xrange(int(raw_input())):
  n,m=map(int,raw_input().split())
  a=[map(lambda x: int(x)-1,raw_input().split()) for _ in xrange(n)]
  print 'Case #%d: %s'%(case+1, 'YES' if f(a) else 'NO')
