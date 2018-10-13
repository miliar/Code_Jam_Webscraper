from collections import deque

def readi():
  return int(input())

def readf():
  return float(input())

def reada(f):
  return [f(x) for x in input().split()]

def readai():
  return reada(int)

def case():
  (R, k, N) = readai()
  G = deque(readai())
  cG = deque(G)
  s = {}
  M = doRide(k, cG)
  count = 1
  #print("caseloop1 {} {} {}".format(count,cG,G))
  while count < R and cG != G:
    #print("caseloop1 {} {} {}".format(count,cG,G))
    count+=1
    M += doRide(k, cG)
  if R == count:
    return M
  cycles = int(R / count)
  count = cycles * count
  #print("caseloop2 {} {}".format(cycles, count))
  M = M*cycles
  while count < R:
    count+=1
    M += doRide(k, cG)
  return M

def doRide(k, G):
  #print("doRide {} {}".format(k,G))
  first = G[0]
  total = 0
  num = 0
  while first + total <= k and num < len(G):
    total += first
    #print("loop {} {} {}".format(total, G, first))
    G.rotate(-1)
    num+=1
    first = G[0]
  return total

for N in range(readi()):
  result = case()
  print("Case #{0}: {1}".format(N + 1, result))
