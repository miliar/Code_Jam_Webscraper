import os.path

def solve(f):
  N,C,M = map(int,f.readline().split(' '))
  B = map(list,[[]]*N)
  for _ in range(M):
    p,b = map(int,f.readline().split(' '))
    B[b-1] += [p]
  F,S = map(sorted,B[:2])
  if len(F)<len(S):
    F,S = S,F
  RES = 0 
  # promo not available  
  while F and F[0]==1:
    F.pop(0)
    RES += 1
    k = 0
    while len(S)>k and S[k]==1:
      k += 1
    if len(S)>k:
      S.pop(k)
  if len(F)<len(S):
    F,S = S,F
  X = 0
  mf = 0
  for n in range(1,1001):
    f = F.count(n)
    s = S.count(n)
    if X<min(f,s):
      X = min(f,s)
    if X==min(f,s):
      mf = max(mf,f)
  m = max(len(F),len(S))
  RES += m    
  return "%d %d" %(RES,max(0,X-(len(F)-mf)))
  
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