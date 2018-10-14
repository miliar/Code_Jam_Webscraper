from fractions import Fraction as Frac

def printout(n, v):
  print "Case #" + str(n) + ": " + str(v)
  
def dictadd(dct, key, val):
  if not dct.has_key(key):
    dct[key] = val
  else:
    dct[key] += val
  
def call():
  n, q = [int(i) for i in raw_input().split()]
  horses = [[float(j) for j in raw_input().split()] for i in range(n)]
  distances = []
  for i in range(n-1):
    distances.append(float(raw_input().split()[i+1]))
  for i in range(q+1):
    raw_input()
  ## nacitance
  avail = [[horses[0][0], horses[0][1], 0]]
  for round in range(n-1):
    newavail = []
    for i in avail:
      if i[0] >= distances[round]:
        newavail.append(i)
    avail = []
    for i in newavail:
      avail.append([i[0] - distances[round], i[1], i[2] + distances[round] / i[1]])
    besttime = float('infinity')
    for i in avail:
      besttime = min(besttime, i[2])
    avail.append([horses[round+1][0], horses[round+1][1], besttime])
  besttime = float('infinity')
  for i in avail:
    besttime = min(besttime, i[2])
  return besttime
    
  
  
  
  
  
t = int(raw_input())
for ii in xrange(t):
  printout(ii+1, call())