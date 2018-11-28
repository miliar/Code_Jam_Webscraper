#! /usr/bin/python

import sys

def solve(N, a_orig, b_orig):
  a_orig = sorted(a_orig)
  b_orig = sorted(b_orig)
  a = a_orig[:]
  b = b_orig[:]
  points_war = 0
  for i in xrange(N):
    m_a = a[-1]
    m_b = b[-1]
    if m_a > m_b:
      points_war += 1
      a.pop(-1)
      b.pop(0)
    else:
      a.pop(-1)
      b.pop(-1)

  a = a_orig
  b = b_orig
  points_deceitful = 0
  for i in xrange(N):
#    print points_deceitful, sorted(a), sorted(b)
    m_a = a[0]
    m_b = b[0]
    if m_a < m_b:
      a.pop(0)
      b.pop(-1)
    else:
      points_deceitful += 1
      a.pop(0)
      b.pop(0)

  return "%d %d" % (points_deceitful, points_war)

fd = open(sys.argv[1])

num_cases = int(fd.readline())

for i in range(0, num_cases):
  N = int(fd.readline())
  naomi = [float(x) for x in fd.readline().strip().split(" ")]
  ken = [float(x) for x in fd.readline().strip().split(" ")]
  output = solve(N, naomi, ken)
  print "Case #%d:" % (i+1), output

