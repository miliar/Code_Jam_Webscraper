import os.path

def solve(f):
  N,P = map(int,f.readline().split(' '))
  R = map(int,f.readline().split(' '))
  Q = []
  for _ in range(N):
    Q += [sorted(map(int,f.readline().split(' ')))]
  I = [0]*N
  p = 1
  RES = 0
  while 1:
    changed = True
    while changed:
      changed = False
      for i in range(N):
        while Q[i][I[i]]*10>R[i]*p*11:
          changed = True
          p += 1
    good = True
    for i in range(N):
      while Q[i][I[i]]*10<R[i]*p*9:
        I[i] += 1
        if I[i]==P:
          return RES
      good &= Q[i][I[i]]*10<=R[i]*p*11
    if good:
      RES += 1
      for i in range(N):
        I[i] += 1
        if I[i] == P:
          return RES
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