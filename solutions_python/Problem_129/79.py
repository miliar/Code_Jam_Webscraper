#!/usr/bin/python

def cost(o, e, N):
  return (e - o)*(o + 1 - e + 2*N)/2


def req(ps, N):
  tc = 0
  for p in ps:
    tc += cost(p[0], p[1], N)*p[2]
  return tc


class Station(object):
  def __init__(self, no):
    self.exit = 0
    self.enter = 0
    self.no = no
  def __str__(self):
    return 'S(%d, %d, %d)' % (self.no, self.enter, self.exit)


def opt(ps, N):
  stations = {}
  for p in ps:
    try:
      s = stations[p[0]]
    except KeyError:
      s = stations[p[0]] = Station(p[0])
    s.enter += p[2]
    try:
      s = stations[p[1]]
    except KeyError:
      s = stations[p[1]] = Station(p[1])
    s.exit += p[2]
  cards = []
  stations = stations.values()
  stations.sort(key = lambda x:x.no)
  tc = 0
  for s in stations:
    if s.enter > s.exit:
      cards.append([s.no, s.enter - s.exit])
    elif s.enter < s.exit:
      to_use = s.exit - s.enter
      while to_use > 0:
        c = min(to_use, cards[-1][1])
        tc += cost(cards[-1][0], s.no, N)*c
        cards[-1][1] -= c
        to_use -= c
        if cards[-1][1] == 0:
          cards.pop()
  return tc



import sys

T = int(sys.stdin.readline().strip())
for t in xrange(1, T + 1):
  N, M = [int(x) for x in sys.stdin.readline().split()]
  ps = []
  for m in xrange(M):
    o, e, p = [int(x) for x in sys.stdin.readline().split()]
    ps.append((o, e, p))
  r1 = req(ps, N)
  r2 = opt(ps, N)
  print 'Case #%d: %d' % (t, (r1 - r2)%1000002013)
