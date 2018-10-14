import sys
# import itertools as it

def main(f):
  T = int(f.next())
  for ti in xrange(T):
    n, k = map(int, f.next().split())
    minp = solve(n, k)
    print "Case #%d: %d %d" % (ti+1, minp[0], minp[1])

def split(n):
  return ((n/2, n/2-1), ((n-1)/2,)*2)[n%2]

def solve0(n, k):
  count = [0]*n+[1]
  m = n
  for i in xrange(k):
    while count[m]==0:
      m -= 1
    count[m] -= 1
    s = split(m)
    # print "split", m, s
    count[s[0]] += 1
    count[s[1]] += 1
  return s

def solve(n, k):
  count = {n: 1}
  while k>0:
    m = max(count.keys())
    q = min(k, count[m])
    count[m] -= q
    if count[m]==0:
      del count[m]
    s = split(m)
    for x in s:
      count[x] = count.get(x,0) + q
    k -= q
  return s

if __name__ == '__main__':
  main(sys.stdin)

