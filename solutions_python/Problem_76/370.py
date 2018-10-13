import sys

def xor(vars):
  s = 0
  for x in vars:
    s = s ^ x
  return s

num_cases = int(sys.stdin.readline())
for x in range(1, num_cases + 1):
  num_candy = int(sys.stdin.readline())
  vars = map(int, sys.stdin.readline().strip().split(" "))
  assert(len(vars) == num_candy)
  print "Case #%d:" % x,
  if xor(vars) != 0:
    print "NO"
  else:
    print sum(vars) - min(vars)
