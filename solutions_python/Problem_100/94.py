#speaking in Tongues
import itertools 
f = open("B-large.in","r")
f2 = open("B-large.out","w")
T = int(f.readline().strip())

def getMin(rs):
  n = len(rs)
  rs.sort()
  
  _min = -1 #if possible n*2
  rmax_star = rs[0][1]
  for i in xrange(n):
    if ( rs[i][1] > rmax_star) :
      rmax_star = rs[i][1]

  tb = [ 0 for i in xrange(n) ] # all value to be 2
  #sum(tb) == star 

  now_star = sum(tb)
  step = 0
  while ( now_star != n*2 ):
    pos = False

    l = [] 
    for i in xrange(n):
      if rs[i][1] <= now_star and tb[i]<2:
        l.append( (tb[i],i) )
    l.sort()
    if ( len(l) > 0 ):
      tb[ l[0][1]] = 2
      step+=1
      pos = True
      now_star = sum(tb)
      continue

    l= []
    for i in xrange(n):
      if rs[i][0] <= now_star and tb[i]==0:
        l.append( (rs[i][1],i) )
    l.sort()
    if ( len(l) > 0 ):
      tb[l[len(l)-1][1]] = 1
      step+=1
      pos = True
      now_star = sum(tb)
      continue
    
    if not pos: 
      return -1
  return step

for TT in xrange(T):
  N = int(f.readline().strip())
  rstar = []
  for i in xrange(N):
    raw = tuple(map(int,f.readline().strip().split()))
    rstar.append(raw)
 
  r = getMin(rstar)
  if r == -1:
    r = "Too Bad"
  f2.write( "Case #%d: %s\n" % ((TT+1), str(r) ) )

f2.close()

f.close()
