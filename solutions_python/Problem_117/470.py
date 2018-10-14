from functools import *

def end(t,c):
  print('Case #' + str(t) + ': ', end='')
  if c:
    print('YES')
  else:
    print('NO')

testcases = int(input())
for tc in range(1, testcases + 1):
  N,M = [int(x) for x in input().split()]
  rows = []
  reqs = []
  for n in range(M):
    reqs.append(999)
  for n in range(N):
    row = [int(x) for x in input().split()]
    rmax = max(row)
    for x in range(len(row)):
      if row[x] < rmax:
        reqs[x] = min(reqs[x],row[x])
    rows.append(row)
  end_state = True
  cols = list(zip(*rows))
  for col in range(len(cols)):
    if (reqs[col] < max(cols[col])):
      end_state = False
    
  end(tc,end_state)
