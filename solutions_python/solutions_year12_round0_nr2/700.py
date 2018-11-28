import sys

T = int(sys.stdin.readline())

def dist(x, y):
  return abs(x-y)

notSurpMax = {}
surpMax = {}

for a in range(11):
  for b in range(11):
    for c in range(11):
      m = max(a, b, c)
      s = a + b + c
      if dist(a,b) <= 2 and dist(a, c) <= 2 and dist(b, c) <= 2:
        if dist(a,b) == 2 or dist(a, c) == 2 or dist(b, c) == 2:
          if s not in surpMax:
            surpMax[s] = m
          else:
            surpMax[s] = max(m, surpMax[s])

        else:
          if s not in notSurpMax:
            notSurpMax[s] = m
          else:
            notSurpMax[s] = max(m, notSurpMax[s])


for t in range(1, T+1):
  vals = map(int, sys.stdin.readline().split())
  N = vals[0]
  S = vals[1]
  p = vals[2]

  scores = vals[3:]

  hadBest = 0
  surpUsed = 0
  notSurpScoreMax = map(lambda x: notSurpMax[x], scores)
  for i in range(len(scores)):
    if notSurpScoreMax[i] >= p:
      hadBest += 1
    elif surpUsed < S and scores[i] in surpMax and surpMax[scores[i]] >= p:
      surpUsed += 1
      hadBest += 1

  print 'Case #%d: %d' % (t, hadBest)
