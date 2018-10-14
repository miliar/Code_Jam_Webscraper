from collections import deque

def isHappy(S):
  all(S)

def hashS(S):
  h = 0
  for b in S :
    h = (h << 2) + b
  
  return h

def nextN(S, K, n):
  f = [not c for c in S[n:n+K]]
  s = S[:n] + f + S[n+K:]
  return (s, hashS(s))
  
def flipBFS(S, K):
  V = set()
  queue = deque([(S, 0)])
  fanN = len(S) - K + 1
  # print(fanN)
  
  while queue :
    c, i = queue.popleft()
    #print(i)

    if all(c) :
      #print(c)
      return i
      
    for j in range(fanN) :
      a, h = nextN(c, K, j)
      # print(a)
      if h not in V :
        V.add(h)
        queue.append((a, i + 1))
        
  return None
        

def solveCase(S, K):
  S = [c == '+' for c in S]

  return flipBFS(S, K)

with open("A-small-attempt0.in") as f :
  T = f.readline()
  T = int(T)
  for i in range(T) :
    c = f.readline()
    S, K = c.split()
    #print(S)
    y = solveCase(S, int(K))
    
    if y is None :
      print("Case #%d: IMPOSSIBLE" % (i + 1))
    else:
      print("Case #%d: %s" % (i + 1, y))
