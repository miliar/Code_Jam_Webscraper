import sys
mod = 1000002013
def f(n, table):
  table.sort()
  starts = {}
  stops = {}
  points = set()
  price1 = 0
  for start, stop, nb in table:
    starts[start] = starts.get(start, 0) + nb
    stops[stop] = stops.get(stop, 0) + nb
    points.add(start)
    points.add(stop)
    dis = stop - start
    price1 += nb * ((n*(n+1)) / 2 - ((n-dis+1)*(n-dis)) / 2)
  points = list(points)
  points.sort()
  price2 = 0
  passengers = 0
  cards = {}
  for p in points:
    to_add = starts.get(p, 0)
    to_sub = stops.get(p, 0)
    cards[-p] = to_add
    remove_cards = []
    l  = list(cards.iteritems())
    l.sort()
    for card, nb in l:
      if to_sub == 0: break
      if card == p: continue
      nb_here = min(nb, to_sub)
      cards[card] -= nb_here
      if nb_here == nb: remove_cards.append(card)
      dis = p + card
      price2 += nb_here * ((n*(n+1)) / 2 - ((n-dis+1)*(n-dis)) / 2)
      to_sub -= nb_here
    for card in remove_cards:
      del cards[card]
  return (price1 - price2) % mod

samples = int(sys.stdin.readline().rstrip())
for i in range(samples):
  [n, m] = sys.stdin.readline().rstrip().split()
  n, m = int(n), int(m)
  table = []
  for j in xrange(m):
    [start, stop, nb] = sys.stdin.readline().rstrip().split()
    start, stop, nb = int(start), int(stop), int(nb)
    table.append((start, stop, nb))
  print "Case #%d: %s" % (i+1, f(n, table))
