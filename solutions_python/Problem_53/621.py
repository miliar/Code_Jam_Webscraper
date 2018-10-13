#/usr/bin/env python3
T=int(input());
for Case in range(1,T+1):
  n,k=map(int,input().split());
  res='ON' if bin(k)[-n:]=='1'*n else 'OFF';
  print('Case #{Case}: {res}'.format(**locals()));
