
T=int(raw_input())
for t in xrange(0,T):
  ans=int(raw_input())
  for i in xrange(1,5):
    l=raw_input()
    if i==ans: s1=set(l.strip().split())
  ans=int(raw_input())
  for i in xrange(1,5):
    l=raw_input()
    if i==ans: s2=set(l.strip().split())
  ints=s1 & s2
  if len(ints)==0: print 'Case #%d: Volunteer cheated!'%(t+1)
  elif len(ints)==1: print 'Case #%d: %s'%(t+1, ints.pop())
  else: print 'Case #%d: Bad magician!'%(t+1)
