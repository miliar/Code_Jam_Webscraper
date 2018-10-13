def check(n):
  n1 = ''.join(sorted(str(n)))
  # print n1,n
  if n!=int(n1):
    n = check(n-1)
  return n
    
t = int(raw_input())
for i in xrange(1,t+1):
  n = int(raw_input())
  print "Case #%d: %d"%(i,check(n))
