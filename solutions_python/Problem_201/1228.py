from  heapq import *

def solve(n, k):
  k -= 1
  h = [-n]
  d = {-n: 1}
  
  while d[h[0]] <= k:
    e = heappop(h)
    a1 = int((e+1) / 2)
    a2 = (e+1) - a1
    if a1 in d:
      d[a1] = d[a1] + d[e]
    else:
      d[a1] = d[e]
      heappush(h,a1)
    if a2 in d:
      d[a2] = d[a2] + d[e]
    else:
      d[a2] = d[e]
      heappush(h,a2)
    k -= d[e]
    del d[e]
    
  e = heappop(h)
  a1 = int((e+1) / 2)
  a2 = (e+1) - a1
  return (-a2, -a1)
  
def solve_int(s, n):
  mins = -88
  maxs = -88
  p = 0
  for i in range(n+2):
    if s[i] == 0:
      l = i
      r = i
      while s[l] == 0:
        l -= 1
      while s[r] == 0:
        r += 1
      l = i - l -1
      r = r - i -1
      if min(l,r) > mins or (min(l,r) == mins and max(l,r) > maxs):
        mins = min(l,r)
        maxs = max(l,r)
        p = i
  return (p, maxs, mins)
  
def solve2(n, k):
  a = [1] + [0] * n + [1]
  for i in range(k-1):
    r = solve_int(a, n)
    a[r[0]] = 1
  r = solve_int(a, n)
  return r[1:]
 
"""
for n in range(1, 100):
   for k in range(1, n):
     r1 = solve(n, k)
     r2 = solve2(n, k)
     if r1[0] != r2[0] or r1[1] != r2[1]:
       print(n,k)
 
    
"""

T = int(input())

for t in range(1, T+1):
  n, k = list(map(int,input().split(' ')))
  r = solve(n,k)
  print("Case #" + str(t) + ":", r[0], r[1]) 

  
