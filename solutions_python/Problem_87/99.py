import sys
def read_values():
  return map(int,raw_input().split())

for case_index in range(1, 1+input()):
  sys.stderr.write(str(case_index)+' ')

  X,S,R,t,N = read_values()
  B = []
  E = []
  w = []
  l = X
  ratio = []
  for _ in range(N):
    bb,ee,ww = read_values()
    B.append(bb)
    E.append(ee)
    w.append(ww)
    ratio.append((ww+S)/(1.0*ww+R))
    l -= ee-bb
  if l:
    N += 1
    B.append(0)
    E.append(l)
    w.append(0)
    ratio.append(S/(1.0*R))
  I = range(N)
  I.sort(key=ratio.__getitem__)
  res = 0
  for k in range(N):
    d = (E[I[k]]-B[I[k]])
    if res>=t:
      res += d/(1.0*w[I[k]]+S)
    else:
      tt = d/(1.0*w[I[k]]+R)
      if res+tt<=t:
        res += tt
      else:
        dd = (t-res)*(w[I[k]]+R)
        res = t+ (d-dd)/(1.0*w[I[k]]+S)
  
  print 'Case #%s: %s'%(case_index,res)

sys.stderr.write('\n')
