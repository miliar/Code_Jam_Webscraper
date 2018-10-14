import sys

rl = lambda : sys.stdin.readline().strip()

def solve_case(case_num):
  answer = int(rl())
  for i in xrange(4):
    line = rl()
    if i == (answer - 1):
      first = set(line.split())

  answer = int(rl())
  for i in xrange(4):
    line = rl()
    if i == (answer - 1):
      second = set(line.split())

  intersec = first & second
  if len(intersec) == 1:
    print "Case #%d: %s" % (case_num, intersec.pop())
  elif len(intersec) > 1:
    print "Case #%d: Bad magician!" % case_num
  else:
    print "Case #%d: Volunteer cheated!" % case_num

def main():
  cases = int(rl())
  for i in xrange(cases):
    solve_case(i + 1)

main()
