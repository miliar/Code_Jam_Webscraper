#!/usr/bin/python -tt
import sys

def is_solvable(size,motes):
  for i in xrange(len(motes)):
    if size > motes[i]: size += motes[i]
    else: return 0
  return 1


def main(A, motes, count):
  #count = 0
  size = A
  
  if size == 1: return len(motes)
  if is_solvable(size,motes): return count

  for i in xrange(len(motes)):
    if size > motes[i]:
      size += motes[i]
    else:
      rest = len(motes) - i

      temp = size
      c = 0
      while temp <= motes[i]:
        temp = 2*temp - 1
        c = c + 1

      #return min(count+rest, main(temp, motes[i:],count))
      if is_solvable(temp,motes[i:]):
        return min(count+rest, count+c)
      else:
        return min(count+rest, main(temp, motes[i:],count+c))

  return count


if __name__ == '__main__':
  T = int(sys.stdin.readline())
  for i in xrange(T):
    A,N = map(int, sys.stdin.readline().strip().split(" "))
    motes = map(int, sys.stdin.readline().strip().split(" "))
    res = main(A, sorted(motes),0)
    print "Case #%d: %s" % (i + 1, res)

