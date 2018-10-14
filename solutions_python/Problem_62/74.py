#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def main():
  f = sys.stdin
  for t in range(int(f.readline())):
    N = int(f.readline())
    wires = []
    for i in range(N):
      wires.append(map(int, f.readline().strip().split(' ')))
    cnt = 0
    for i in range(N):  # i => cur
      for j in range(N):
        if i != j:
          if wires[i][0] < wires[j][0] and wires[i][1] > wires[j][1]:
            cnt += 1
          elif wires[i][0] > wires[j][0] and wires[i][1] < wires[j][1]:
            cnt += 1
    cnt /= 2
    print 'Case #%d: %d' % (t+1, cnt)

if __name__ == '__main__':
  main()
