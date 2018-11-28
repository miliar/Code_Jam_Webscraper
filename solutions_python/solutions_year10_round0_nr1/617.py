#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def main():
  for i, line in enumerate(sys.stdin):
    if i == 0:
      continue

    (N, K) = map(lambda x: int(x), line.split(' '))
    ans = False
    if K % 2:
      calc = (long(K / 2) + 1) % pow(2, N - 1)
      if calc == 0:
        ans = True
        
    print "Case #%d: %s" % (i, "ON" if ans else "OFF")

if __name__ == '__main__':
  main()
