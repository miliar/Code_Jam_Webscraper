#!/usr/bin/python

import sys

def parse(f):
  return f.readline().rstrip()

def solve(s):
  ch2n = dict()
  npool = [1,0] + range(2, 100)
  ni = 0
  for ch in s:
    if not ch in ch2n:
      ch2n[ch] =  npool[ni]
      ni+=1
  digits = map(lambda ch: ch2n[ch], s)
  radix = ni
  if radix < 2:
    radix = 2
  # print "digits=%s radix=%d" % (str(digits), radix)
  return to10(digits, radix)

def to10(digits, radix):
  m = 1
  n = 0
  for digit in digits[::-1]:
    n += digit*m
    m *= radix
  return n

def main():
  f = sys.stdin
  n = int(f.readline())
  for i in range(n):
    o = parse(f)
    print 'Case #%d: %d' % (i+1, solve(o))

if __name__ == '__main__':
  main()
