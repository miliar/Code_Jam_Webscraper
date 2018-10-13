from base import *

import math

def case():
  n = int(input())
  strs = [input() for i in range(n)]
  counts = []
  smashed = list(map(lambda s: smash(s, counts), strs))
  smashBase = smashed[0]
  for s in smashed:
    if smashBase != s:
      return 'Fegla Won'
  total = 0
  for i in range(len(smashBase)):
    letter = smashBase[i]
    curcounts = [c[i] for c in counts]
    mid = math.floor(mean(curcounts))
    total += min(distance(mid, curcounts), distance(mid+1,curcounts))
  return total

def mean(l):
  return sum(l) / len(l)

def distance(chosen, l):
  dist = 0
  for i in l:
    dist += abs(i-chosen)
  return dist

def smash(s, allcounts):
  ret = []
  prev = None
  counts = []
  for i in s:
    if i != prev:
      ret.append(i)
      prev = i
      counts.append(1)
    else:
      counts[len(counts)-1] += 1
  allcounts.append(counts)
  return ''.join(ret)

if __name__ == '__main__': main(case)