#!/usr/bin/python2

def solve():
  first = int(raw_input())
  for y in xrange(4):
    nums = map(int, raw_input().split())
    if first == y+1:
      s1 = set(nums)

  second = int(raw_input())
  for y in xrange(4):
    nums = map(int, raw_input().split())
    if second == y+1:
      s2 = set(nums)

  inter = s1 & s2
  if len(inter) == 0:
    return 'Volunteer cheated!'
  elif len(inter) != 1:
    return 'Bad magician!'
  else:
    return list(inter)[0]

cases = int(raw_input())
for test in xrange(cases):
  ans = solve()
  print 'Case #%d: %s' % (test+1, ans)
