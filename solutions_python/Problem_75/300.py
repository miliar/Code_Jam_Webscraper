#!/usr/bin/python
import sys
T = int(sys.stdin.readline())
for t in range(T):
  n = 0
  v = sys.stdin.readline().split()
  
  C = int(v[n])
  n += 1
  combinations = {}
  for c in range(C):
    key = v[n][:2]
    val = v[n][-1:]
    combinations[key] = val
    combinations[key[1]+key[0]] = val
    n += 1
  
  D = int(v[n])
  n += 1
  opposed = {}
  for d in range(D):
    a = v[n][0]
    b = v[n][1]
    if a not in opposed:
      opposed[a] = [b]
    else:
      opposed[a].append(b)
    if b not in opposed:
      opposed[b] = [a]
    else:
      opposed[b].append(a)
    n += 1
  
  N = int(v[n])
  n += 1
  sequence = v[n]
  result = ""
  for i in range(0, N):
    result += sequence[i]
    while result[-2:] in combinations:
      result = result[:-2] + combinations[result[-2:]]
    if result[-1] in opposed:
      for j in opposed[result[-1]]:
        if len(result) > 0 and result.find(j) >= 0:
          result = ""
          break
  
  print "Case #%d: [%s]" % (t+1, ", ".join(list(result)))