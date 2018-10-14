def kth(n,k):
 if n == k: return 0, 0
 t = [1] + [0 for i in xrange(n)] + [1]
 for i in xrange(k):
  p = [(-1,-1) for j in xrange(n+2)]
  for j in xrange(n+2):
   if t[j] == 0:
    l = 0
    while t[j-l-1] == 0:
     l += 1
    r = 0
    while t[j+r+1] == 0:
     r += 1
    p[j] = (l,r)
  q = [min(l,r) for (l,r) in p]
  Q = [max(l,r) for (l,r) in p]
  m = max(q)
  r = [j for j in xrange(n+2) if q[j] == m]
  M = max(Q[j] for j in xrange(n+2) if j in r)
  s = [j for j in r if Q[j]==M]
  t[min(s)] = 1
 return p[min(s)]


fname = "C-small-1-attempt1"


with open(fname + ".in","r") as f:
 inp = [l.strip('\n') for l in f.readlines()]

f = open(fname + ".out","w")
for i in range(int(inp[0])):
 j = i+1
 data = inp[j].split(' ')
 result = kth(int(data[0]),int(data[1]))
 f.write("Case #" + str(j) + ": " + str(max(result)) + " " + str(min(result)) + "\n")

f.close()
