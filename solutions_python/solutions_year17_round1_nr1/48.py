import os.path

def pg(G):
  for g in G:
    print "".join(g)
    

def solve(f):
  R,C = map(int,f.readline().split(' '))
  G = []
  for _ in range(R):
    G += [list(f.readline().rstrip())]
  for i in range(R):
    for j in range(C):
      if G[i][j] != '?':
        k = j-1
        while k>=0 and G[i][k]=='?':
          G[i][k] = G[i][j]
          k -= 1
        k = j+1
        while k<C and G[i][k]=='?':
          G[i][k] = G[i][j]
          k += 1
  for g in G:
    if g[0] != '?':
      L = g
      break
  R = []
  for g in G:
    if g[0] == '?':
      R += [L]
    else:
      L = g
      R += [g]
  RES = ""
  for r in R:
    RES += "\n"+"".join(r)      
  return RES
  
def out(s):
  print s
  o.write(s)
  
if os.path.exists("input.in"):
  f = open("input.in")
else:
  f = open("input-sample.in")
o = open("output.out", "wt")
T = int(f.readline())
for t in range(T):
  out("Case #%d: %s" %(t+1,solve(f)))
  o.write('\n')
o.close()