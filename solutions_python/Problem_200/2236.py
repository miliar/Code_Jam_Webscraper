import sys


def cin():
  return sys.stdin.readline().strip()


def readlist():
  return map(int, cin().split())


INF = sys.maxsize
NINF = -sys.maxsize - 1

#----------------------------------------------------------------------


def so(c):
  assert c != '0'
  return chr(ord(c) - 1)


T = int(cin())
for _t in xrange(T):
  N = cin()
  N = list(reversed(list(N)))
  i = 0
  while i < len(N):
    for j in xrange(i + 1, len(N)):
      if not (N[i] >= N[j]):
        k = j
        while N[k] == '0':
          k += 1
        N[k] = so(N[k])
        for a in xrange(k):
          N[a] = '9'
    i += 1

  N = ''.join(reversed(N))
  # trim leading zeroes!
  N = N.lstrip('0')
  print "Case #{}: {}".format(_t + 1, N)
