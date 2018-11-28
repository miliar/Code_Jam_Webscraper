def doe(eerst, toe):
  X = set()
  
  def addp(s, b):
    c = 0
    m = s.split("/")[1:]
    l = len(m)
    for i in range(l):
      ss = "/".join(m[:i+1])
      if not ss in X:
        X.add(ss)
        if b: c += 1
    return c
  cost = 0
  for i in eerst: addp(i, 0)
  for i in toe:   cost += addp(i, 1)
  
  return cost

T = int(raw_input(""))
for t in range(T):
  N, M = map(int, raw_input("").split())
  ss = [raw_input("") for i in range(N)]
  tt = [raw_input("") for i in range(M)]
  print "Case #%d: %d" % (t+1, doe(ss, tt))
