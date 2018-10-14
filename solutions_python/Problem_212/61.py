import os.path

def solve(f):
  N,P = map(int,f.readline().split(' '))
  G = map(int,f.readline().split(' '))
  Z = [0]*P
  for g in G:
    Z[g%P] += 1
  RES = 0
  RES += Z[0]
  if P==2:
    RES += (Z[1]+1)/2
  if P==3:
    m = min(Z[1],Z[2])
    RES += m
    Z[1] -= m
    Z[2] -= m
    RES += (Z[1]+Z[2]+2)/3
  if P==4:
    RES += Z[2]/2
    Z[2] %= 2
    m = min(Z[1],Z[3])
    RES += m
    Z[1] -= m
    Z[3] -= m
    r = Z[1]+Z[3]
    if Z[2]>0:
      RES += 1
      r = max(r-2,0)
    RES += (r+3)/4      
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