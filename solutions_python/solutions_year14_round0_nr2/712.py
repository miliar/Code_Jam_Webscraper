for t in xrange(input()):
 C,F,X = map(float,raw_input().split())
 
 
 r = 2.0
 ans = X/r
 time = 0.0
 for i in xrange(int(X)+1):
  ans = min(ans,time+X/r)
  time+=C/r
  r+=F
 print "Case #%d: %.7f"%(t+1,ans)