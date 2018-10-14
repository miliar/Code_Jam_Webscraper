import sys
import re

def nextint():
  return int(sys.stdin.readline().strip())

def nextintpair():
  pair = sys.stdin.readline().strip().split(" ")
  assert len(pair) == 2
  return int(pair[0]), int(pair[1])

def testcase_read():
  regexp = re.compile('^(\d\d):(\d\d) (\d\d):(\d\d)$')
  t = nextint()
  na, nb = nextintpair()
  qa = []
  qb = []
  for i in xrange(na + nb):
    match = regexp.match(sys.stdin.readline())
    assert match
    a = int(match.group(1)) * 60 + int(match.group(2))
    b = int(match.group(3)) * 60 + int(match.group(4))
    if i < na:
      qa.append((a, 1))
      qb.append((b + t, 0))
    else:
      qb.append((a, 1))
      qa.append((b + t, 0))
  qa.sort()
  qb.sort()
  return dict(t=t, na=na, nb=nb, qa=qa, qb=qb)

def solve(queue):
  deficit = 0
  max_deficit = 0
  for p, direction in queue:
    if 1 == direction:
      deficit += 1
    else:
      deficit -= 1
    max_deficit = max(deficit, max_deficit)
  return max_deficit

def main():
  for zi in xrange(nextint()):
    testcase = testcase_read()
    print >> sys.stderr, testcase
    print 'Case #%d: %d %d' % ( zi + 1, solve(testcase['qa']),
                                solve(testcase['qb']) )

if "__main__" == __name__:
  main()

