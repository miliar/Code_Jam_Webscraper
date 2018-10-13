T = int(input())

for i in range(1,T+1):
  N, C, M = map(int, input().split())
  P = []
  B = []
  for _ in range(M):
    a,b = map(int, input().split())
    P.append(a)
    B.append(b)
  dP = dict()
  for p in range(1,N+1):
    dP[p] = []
  dB = dict()
  for b in range(1,C+1):
    dB[b] = []
  for p,b in zip(P,B):
    dP[p].append(b)
    dB[b].append(p)
  total = max([len(dB[b]) for b in B]) 
  change = 0
  total = max(total, len(dP[1]))
  sp = len(dP[1])
  for p in range(2,N+1):
    sp += len(dP[p])
    total = max(total, (sp+p-1)//p)
  for p in range(2,N+1):
    if len(dP[p]) > total:
      change += len(dP[p]) - total
  print('Case #{}: {} {}'.format(i,total,change))

