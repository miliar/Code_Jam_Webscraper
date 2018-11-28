import sys
sys.stdin = open('A-small-attempt0.in')
sys.stdout = open('A-small-attempt0.out', 'w')
rd = lambda : map(int, raw_input().split())
rdmat = lambda : [rd(), rd(), rd(), rd()]
t = input()
for case in range(t):
  r1 = input()
  m1 = rdmat()
  r2 = input()
  m2 = rdmat()
  res = set(m1[r1 - 1]).intersection(set(m2[r2 - 1]))
  if len(res) == 0:
    print 'Case #%d: Volunteer cheated!' % (case + 1)
  elif len(res) > 1:
    print 'Case #%d: Bad magician!' % (case + 1)
  else:
    print 'Case #%d: %d' % (case + 1, res.pop())
  
