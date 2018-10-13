import sys

def getint():
  return int(sys.stdin.readline())

def getints():
  return [int(s) for s in sys.stdin.readline().split()]

class Ring(object):

  def __init__(self, items):
    self.items = items
    self.pos = 0

  def get(self):
    item = self.items[self.pos]
    self.pos += 1
    self.pos %= len(self.items)
    return item

  def curr(self):
    return self.items[self.pos]

  def start(self):
    self.startpos = self.pos

  def isempty(self):
    return self.startpos == self.pos

def solve(R, k, g):
  gr = Ring(g)
  income = 0

  cache = dict()

  while R:

    k0 = 0
    gr.start()
    while 1:
      if k0 + gr.curr() > k:
        break
      k0 += gr.get()
      if gr.isempty():
        break

    income += k0

    R -= 1

    for pos in cache:
      cache[pos] = cache[pos][0]+k0, cache[pos][1]+1
#      print 'CACHE ADD cache[%d]=%r' % (pos, cache[pos])

    if gr.pos in cache:
#      print 'CACHE SUCCESS cache[%d]=%r' % (gr.pos, cache[gr.pos])
      sum, i = cache[gr.pos]
      if R > i:
        n = R // i
        income += sum * n
        R -= i * n
#        print 'CACHE USE n=%d, income: %d + %d = %d' % (n, income-sum*n, sum*n, income)
        continue
    else:
      cache[gr.pos] = (0, 0) # (sum, index)
#      print 'CACHE INIT cache[%d]=%r' % (gr.pos, cache[gr.pos])

  return income

T = getint()
for i in range(T):
  R, k, N = getints()
  g = getints()
  assert len(g) == N
  print 'Case #%d: %s' % (i+1, solve(R, k, g))
