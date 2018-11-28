#!/usr/bin/python

import heapq

def distCost(d, n):
  return d * n - (d * (d - 1)) / 2

def main():
  t = int(raw_input())
  for case in range(1, t + 1):
    n, m = [int(_) for _ in raw_input().split(' ')]
    places = set()
    on = dict()
    off = dict()
    total = 0
    #print 'n = %d m = %d' % (n, m)
    #print 'Case #%d: 12' % case
    for i in range(m):
      a, b, p = [int(_) for _ in raw_input().split(' ')]
      places.add(a)
      places.add(b)
      on[a] = on.get(a, 0) + p
      off[b] = off.get(b, 0) + p
      total += p * distCost(b - a, n)
      #print 'a = %d b = %d c = %d' % (a, b, p)

    cost = 0
    pq = []
    places = list(places)
    places.sort()
    for p in places:
      heapq.heappush(pq, [-p, on.get(p, 0)])
      cnt = off.get(p, 0)
      while cnt > 0:
        top = heapq.heappop(pq)
        dist = p - (-top[0])
        if top[1] <= cnt:
          cost += top[1] * distCost(dist, n)
          cnt -= top[1]
        else:
          cost += cnt * distCost(dist, n)
          top[1] -= cnt
          cnt = 0
          heapq.heappush(pq, top)

    print 'Case #%d: %d' % (case, total - cost)

if __name__ == '__main__':
  main()

