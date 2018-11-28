import sys
import itertools as it

def main(f):
  T = int(f.next())
  for ti in xrange(T):
    s, k = f.next().strip().split()
    minp = solve(s, int(k))
    print "Case #%d: %s" % (ti+1, minp)

def solve(s, k):
  # print s, k
  n = len(s)
  v = [ int(x=="+") for x in s ]
  # if sum(v) == n:
  #   return 0
  # elif sum(v[n-k:k]) in [0, 2*k-n]:
  #   print v[n-k:k], sum(v[n-k:k])
  #   return "IMPOSSIBLE"
  count = 0
  for p in xrange(0, n-k+1):
    if v[p] == 1:
      continue
    for i in xrange(k):
      v[p+i] =  1 - v[p+i]
    count += 1
    # print "p", p, v
  if sum(v[-k:]) < k:
    return "IMPOSSIBLE"
  return count

if __name__ == '__main__':
  main(sys.stdin)
