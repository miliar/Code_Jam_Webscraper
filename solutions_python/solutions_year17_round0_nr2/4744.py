def decrement(S):
  s = len(S)
  D = []
  d = -1
  for n in reversed(S):
    n = n + d
    if n < 0 :
      n = 9
    else :
      d = 0
    
    D.append(n)
  
  D.reverse()
  
  return D
    

def solveCase(S):
  while True :
    if all(a <= b for a, b in zip(S[:-1], S[1:])) :
      return "".join([str(n) for n in S]).lstrip('0')
    else :
      S = decrement(S)
      # print(S)
  

with open("B-small-attempt1.in") as f :
  T = f.readline()
  T = int(T)
  for i in range(T) :
    l = f.readline().strip()
    S = [int(c) for c in l]
    
    y = solveCase(S)
    
    print("Case #%d: %s" % (i + 1, y))
