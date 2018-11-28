#!/usr/bin/env python

def judge(matrx, N, M):
  for i in range(N):
    maxh = max(matrx[i])
    for j in range(M):
      if matrx[i][j] < maxh:
        for k in range(N):
          if matrx[k][j] > matrx[i][j]:
            return "NO"
  return "YES"
        
def main():
  cases = int(raw_input())
  for case in range(cases):
    case = case + 1
    tups = raw_input().split()
    N = int(tups[0])
    M = int(tups[1])
    matrx = []
    for i in range(N):
      tups = raw_input().split()
      row = [int(x) for x in tups]
      matrx.append(row)
    print "Case #%d: %s" % (case, judge(matrx, N, M))

main()
