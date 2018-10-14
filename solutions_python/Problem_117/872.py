#!/usr/bin/python
import sys

def checklawn(lawn):
  #print lawn
  n = len(lawn)
  m = len(lawn[0])
  init = [[100]*m]*n
  #print init
  for i in range(n):
    maximum = max(lawn[i])
    init[i] = [min(a, maximum) for a in init[i]]
  #print init
  for j in range(m):
    maximum = max([row[j] for row in lawn])
    #print [a[j] for a in lawn], maximum
    for i in range(n):
      init[i][j] = min(init[i][j], maximum)

  for i in range(n):
    for j in range(m):
      if init[i][j] != lawn[i][j]:
        return 'NO'
  return 'YES' 

def main():
  case = int(sys.stdin.readline())
  for i in range(case):
    line = sys.stdin.readline().strip()
    N = int(line[:line.find(' ')])
    M = int(line[line.find(' '):])
    lawn = []
    for j in range(N):
      line = sys.stdin.readline().strip().split(' ')
      hs = []
      for h in line:
        hs.append(int(h))
      lawn.append(hs)
    #print N, M, lawn
    rlt = checklawn(lawn)
    print 'Case #%d: %s' % (i+1, rlt)

if __name__ == '__main__':
  main()
