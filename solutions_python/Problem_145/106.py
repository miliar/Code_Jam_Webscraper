import math

def nwd(a, b):
  while b:
    a, b = b, a%b
  return a

T = input()
for t in range(1,T+1):
  p,q = map(int,raw_input().split("/"))
  com = nwd(p,q)
  p /= com
  q /= com
  result = math.ceil(math.log(float(q)/float(p),2))
  if math.log(q,2)%1 == 0.0:
    print "Case #%d: %d" % (t,result)
  else:
    print "Case #%d: impossible" % t
