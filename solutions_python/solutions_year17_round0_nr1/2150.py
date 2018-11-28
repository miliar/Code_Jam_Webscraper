import sys
T = int(sys.stdin.readline())
for itr in range(T):
  pc, k = sys.stdin.readline().strip().split(" ")
  pc = list(map(lambda c: c=='+', pc))
  k = int(k)
  flips = 0
  for i in range(len(pc)-k+1):
    if not pc[i]:
      flips += 1
      for j in range(k):
        pc[i+j] = not pc[i+j]
  res = flips if all(pc) else 'IMPOSSIBLE'
  print('Case #{}: {}'.format(itr+1, res))