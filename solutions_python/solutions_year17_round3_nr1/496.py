import sys
import math
sys.stdin = open('/Users/tin/Downloads/A-large.in', 'r')
sys.stdout = open('A-large', 'w')

def choose(N, K, pankages, begin):
  if K == 0:
    return 0
  p = sorted(pankages[begin:], key=lambda x: x[1] * x[0], reverse=True)
  kk = 0
  for i in xrange(K):
    kk += p[i][1] * p[i][0] * 2

  return kk


def solve(N, K, pankages):
  m = 0
  for i in xrange(0, N - K + 1):
    r = choose(N, K - 1, pankages, i + 1)
    r = pankages[i][0] ** 2 + 2 * pankages[i][0] * pankages[i][1] + r
    m = max(r, m)
  return m

if __name__ == "__main__":

  T = input()
  for t in xrange(1, T + 1):
    N, K = map(int, raw_input().split(" "))
    pankages = []
    for k in xrange(N):
      R, H = map(int, raw_input().split(" "))
      pankages.append((R, H))
    pankages = sorted(pankages, reverse=True)
    r = solve(N, K, pankages) * math.pi
    r = "{0:.10f}".format(r)
    print "Case #" + str(t) + ": " + str(r)
