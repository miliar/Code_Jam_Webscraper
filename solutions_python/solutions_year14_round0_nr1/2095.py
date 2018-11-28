#!/usr/bin/python -tt

def main(firstq, firstd, secondq, secondd):
  posib1 = firstd[firstq - 1]
  posib2 = secondd[secondq - 1]

  repet = []
  r = ""

  for j in posib1:
    if j in posib2: repet.append(j)

  if len(repet) == 0: r = "Volunteer cheated!"
  elif len(repet) == 1: r = str(repet[0])
  else: r = "Bad magician!"

  return r


if __name__ == '__main__':
  import sys
  T = int(sys.stdin.readline())
  for i in xrange(T):
    firstq = int(sys.stdin.readline())
    firstd = []
    for j in xrange(4):
      firstd.append(map(int,sys.stdin.readline().strip().split(" ")))

    secondq = int(sys.stdin.readline())
    secondd = []
    for j in xrange(4):
      secondd.append(map(int,sys.stdin.readline().strip().split(" ")))

    res = main(firstq, firstd, secondq, secondd)
    print "Case #%d: %s" % (i + 1, res)

