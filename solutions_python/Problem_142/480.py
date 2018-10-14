import itertools

def solve(A):
  B = None
  s = 0
  NS = []
  for a in A:
    T = itertools.groupby(a)
    t = ''
    u = []
    for x, y in T:
      t += x
      y = list(y)
      u.append(len(y))
      s += len(y) - 1
    NS.append(u)

    if B == None:
      B = t
    else:
      if t == B:
        continue
      else:
        return 'Fegla Won'
  NS = zip(*NS)
  MS = []
  for i in NS:
    MS.append(((max(i) + min(i))/2))
  KS = []
  ks = 0
  for i, xs in zip(MS, NS):
    z = 0
    for j in xs:
      z += abs(j - i)
    ks += z
  return ks


def main():
  T = int(raw_input())
  for t in xrange(1, T+1):
    N = int(raw_input())
    A = []
    for i in xrange(N):
      A.append(raw_input())
    print 'Case #{0}: {1}'.format(t, solve(A))

if __name__ == '__main__':
  main()
