# rynkruger@gmail.com

cases = int(raw_input())
for x in range(1,cases+1):
  inp = raw_input().split(" ")
  n = int(inp[0])
  k = int(inp[1])
  full=(2**(n-1))*2-1
  ans = k &full
  if ans==full:
    y="ON"
  else:
    y="OFF"
  print "Case #%d: %s"%(x,y)
