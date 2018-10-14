import sys

inp = sys.stdin

def solve_war(n,naomi,ken):
  points=0
  #naomi.sort()
  ken.sort()
  for n in naomi:
    if(ken[-1]<n):  
      del ken[0]
      points+=1
    else:
      i=0
      while(ken[i]<n): i+=1
      del ken[i]
  return points

def solve_delight(n,naomi,ken):
  ken.sort()
  naomi.sort()
  points=0
  for k in ken:
    for (i,n) in enumerate(naomi):
      if n>k:
        del naomi[i]
        points+=1
        break
  return points

def solve(n,naomi,ken):
  return solve_delight(n,list(naomi),list(ken)),solve_war(n,naomi,ken)
    

T=int(inp.readline())
for t in range(1,T+1):
  n= int(inp.readline()) 
  naomi = [float(y) for y in inp.readline().split()]
  ken   = [float(y) for y in inp.readline().split()]
  d,w = solve(n,naomi,ken)
  print "Case #%d: %d %d" % (t,d,w)

