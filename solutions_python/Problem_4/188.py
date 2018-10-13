import sys, math

inputcases = int(sys.stdin.readline())
for caseno in range(inputcases):
  print 'Case #%d:' % (caseno+1),

  n = int(sys.stdin.readline())
  
  v1 = map(int, sys.stdin.readline().split())
  v2 = map(int, sys.stdin.readline().split())

  v1.sort()
  v2.sort()
  
  total = 0

  v1neg = min(len([i for i in v1 if i <= 0]), len([i for i in v2 if i > 0]))
  v2neg = min(len([i for i in v2 if i <= 0]), len([i for i in v1 if i > 0]))

  for i in range(v1neg):
    total += v1[i] * v2[-i-1]
  for i in range(v2neg):
    total += v2[i] * v1[-i-1]

  left = len(v1) - v1neg - v2neg

  v1left = v1[v1neg:v1neg+left]
  v2left = v2[v2neg:v2neg+left]
  v1left.sort()
  v2left.sort()

  combined = v1left + v2left
  combined.sort()
  combined = combined[:len(v1left)]
  for pick in combined:
    if v1left.count(pick) > 0 and v2left.count(pick) > 0:
      if v1left[-1] > v2left[-1]: # use biggest from v1
        total += v1left.pop() * v2left.pop(0)
      else:
        total += v1left.pop(0) * v2left.pop()
    elif v1left.count(pick) > 0 :
      total += v1left.pop(0) * v2left.pop()
    else:
      total += v1left.pop() * v2left.pop(0)
     
  print total
