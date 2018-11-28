T = int(raw_input())

for t in xrange(T):
  ans = ""
  n,k = map(int,raw_input().split())
  
  #if k==0:
    #ans = "OFF"
  #else:
  if (k+1)%pow(2,n) == 0:
    ans = "ON"
  else:
    ans = "OFF"
  
  print "Case #"+str(t+1)+":",ans