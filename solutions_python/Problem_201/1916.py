#!/usr/bin/env python3

def split(n):
  if n%2:
    a = int((n-1)/2)
    return a,a
  else:
    a = int(n/2)
    return a,a-1

def bathroom_stalls(stalls,k):
  a,b= 0,0
  for i in range(k):
    n = stalls[i]
    a,b = split(n)
    stalls.append(a)
    stalls.append(b)
    stalls=list(reversed(sorted(stalls)))
    if a<1 and b<1:
      break
  return a,b

T = int(input())
for i in range(1,T+1):
  line = input()
  N, K = map(int,line.split())
  y_max, z_min = bathroom_stalls([N],K)
  print('Case #{}: {} {}'.format(i,y_max,z_min))

