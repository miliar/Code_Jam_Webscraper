def are_equal(n, m, offset = 0):
  length = len(n)
  for x in xrange(length):
    if n[x] != m[(x + offset) % length]:
      return False
  return True

def recycled(n, m):
  for x in xrange(len(m)):
    if are_equal(n, m, x):
      return True
  return False

def num_recycled(n, m):
  count = 0
  for a in xrange(n, m):
    for b in xrange(a + 1, m + 1):
      count += 1 if recycled(str(a), str(b)) else 0
  return count

cases = int(raw_input())  # Number of test cases
for x in xrange(cases):
  n, m = raw_input().split()
  n, m = int(n), int(m)
  print "Case #%i: %i" % (x + 1, num_recycled(n, m))
