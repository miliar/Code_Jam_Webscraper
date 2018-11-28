def f(R,k,N,g):
 if sum(g) <= k: return R*sum(g)
 tot,pos = 0,0
 for i in xrange(R):
  people = 0
  while people + g[pos] <= k:
   tot, people, pos = tot+g[pos], people+g[pos], (pos + 1) % N
 return tot

for j in xrange(1,int(raw_input())+1):
 [l1,l2] = [[int(z) for z in raw_input().split()] for p in [0,0]]
 print "Case #%d: %d" % (j,f(l1[0],l1[1],l1[2],l2))

