#!/usr/bin/python3

import sys

def solve(smax, slist):
  tot = slist[0]
  need = 0
  for i in range(smax):
    diff = i - tot + 1
    tot += slist[i + 1] 
    if diff > 0:
      need += diff
      tot += diff
  return need

def main():
  case = 1
  sys.stdin.readline()
  for line in sys.stdin:
    l = line.split()
    smax = int(l[0])
    slist = [int(n) for n in l[1]]
    print('Case #{}: {}'.format(case, solve(smax, slist)))
    case += 1
    
if __name__ == "__main__":
  main()
