def yz(s, stalls):
  g = len(stalls)
  l = 0
  r = 0
  while True:
    if s+r+1 >= g:
      break
    if stalls[s+r+1] == 0:
      r += 1
    else:
      break
  while True:
    if s-l-1 < 0:
      break
    if stalls[s-l-1] == 0:
      l += 1
    else:
      break
  return (min(l,r), max(l,r))
  
for _ in range(int(input())):
  n, k = [int(i) for i in input().split()]
  stalls = [0 for i in range(n+2)]
  stalls[0] = 1
  stalls[-1] = 1
  for i in range(k):
    bests = 0
    best = (0, 0)
    for s in range(1, n+1):
      if stalls[s] == 0:
        gg = yz(s, stalls)
        if yz(s, stalls) > best:
          best = gg
          bests = s
    stalls[bests] = 1
    if i == k-1:
      print("Case #" + str(_ + 1) + ":", best[1], best[0])
    
  