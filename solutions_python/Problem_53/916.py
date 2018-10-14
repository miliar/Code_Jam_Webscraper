import sys
import psyco
from collections import deque
psyco.full()

def ReadInts():
  return list(map(int, sys.stdin.readline().strip().split(" ")))

def ReadInt():
  return int(sys.stdin.readline().strip())

def PowerLength(s):
  N = len(s)
  powerLength = 0
  i = 0
  while i < N:
    if s[i]:
      powerLength += 1
      i += 1
    else:
      i = N
  if len(s) == powerLength:
    return powerLength - 1
  return powerLength


def snap(s):
  p = PowerLength(s)
  if p > 0:
    for i in xrange(p+1):
      s[i] = not s[i]
  else:
    s[0] = not s[0]
  return s

def main():
  T = ReadInt()
  for _ in xrange(T):

    N,K = ReadInts()
    s = [0]*N
    for switch in xrange(K):
      s = snap(s)
    out = "OFF"
    if len(s) - 1 == PowerLength(s) and s[-1]:
      out = "ON"
    print "Case #%d: %s" %(_+1, out)

main()
