import math
f = open("i1.2")
t = int(f.readline())
  
for tt in range (1, t+1):
  d = int(f.readline())
  p = map(int, f.readline().split())
  def s(i):
    pp = map(lambda pi:math.ceil(float(pi)/i)-1, p)
    return reduce(lambda x,y: x+y, pp)
  m = max(p)
  for i in range(1, max(p)+1):
    mm = s(i) + i
    if mm<m:
      m=mm
  print "Case #" + str(tt) + ": " + str(int(m))
