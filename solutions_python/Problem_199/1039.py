from time import time

inp = open('a.in', 'r+')
out = open('a.out', 'w')

T = int(inp.readline())

for t in range(T):
  s = inp.readline().strip().split(' ')
  c = [x == '+' for x in s[0]]
  k = int(s[1])
  swaps = 0
  for i in range(len(c) - k + 1):
    if not c[i]:
      swaps += 1
      for p in range(k):
        c[i+p] = not c[i+p]
  
  good = True
  for p in range(k):
    good = good and c[len(c) - k + p ]
  o = swaps if good else "IMPOSSIBLE"
  out.write("Case #"+str(t+1)+": "+str(o)+"\n")

out.close()