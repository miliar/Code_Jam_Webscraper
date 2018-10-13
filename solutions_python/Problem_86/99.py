#!/usr/bin/python
import sys

def calc(notes, low, high):
  notes.sort()
  for i in xrange(low, high+1):
    for n in notes:
      if ((n >= i and n%i != 0) or
          (n <= i and i%n != 0)):
        break
    else:
      return i
  return "NO"

def main(filename):
  f = file(filename)
  n = int(f.readline())
  for case in xrange(1, n+1):
    N,L,H = map(int, f.readline().split())
    notes = map(int, f.readline().split())
    print "Case #%d: %s" % (case, calc(notes, L, H))

if __name__ == "__main__":
  main(sys.argv[1])
