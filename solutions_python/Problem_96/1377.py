import sys, re, math

def solve(S, p, ts):
  def p1(t):
    return max(p - 1, 0) * 3 + 1 <= t or p * 3 <= t
  def p2(t):
    return not p1(t) and max(p - 2, 0) * 3 + 2 <= t
  k1 = len([t for t in ts if p1(t)])
  k2 = len([t for t in ts if p2(t)])
  return k1 + min(k2, S)

def main(args):
  T = int(sys.stdin.readline())
  for _ in range(T):
    ss = sys.stdin.readline().split()
    N = ss[0]
    S = int(ss[1])
    p = int(ss[2])
    ts = [int(t) for t in ss[3:]]
    a = solve(S, p, ts)
    print('Case #{0}: {1}'.format(_ + 1, a))


main(sys.argv)
