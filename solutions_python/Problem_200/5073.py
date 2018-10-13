def istidy(n):
  ns = str(n)
  for i in xrange(0, len(ns) - 1):
    if(int(ns[i]) > int(ns[i+1])):
      return False
  return True

def solve(i, n):
  while(not istidy(n)):
    n = n - 1
  print "Case #{}: {}".format(i, n)

# Amount of testcases
t = int(raw_input())

# Read per case
for i in xrange(1, t + 1):
  n = int(raw_input())
  solve(i, n)

