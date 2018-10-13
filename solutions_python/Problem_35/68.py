import sys

class Cell:
  def __init__(self, alt):
    self.alt = alt
    self.label = None

class Map:
  def __init__(self):
    (h, w) = map(lambda x: int(x), sys.stdin.readline().strip().split(" "))
    self.h = h
    self.w = w
    self.cells = []
    self.label_offset = 0
    for i in xrange(0, h):
      row = []
      for alt in map(lambda x: int(x), sys.stdin.readline().strip().split(" ")):
        row.append(Cell(alt))
      self.cells.append(row)

  def Get(self, x, y):
    if x < 0 or x >= self.w or y < 0 or y >= self.h:
      return None
    return self.cells[y][x]

  def LinkToLower(self):
    for y in xrange(0, self.h):
      for x in xrange(0, self.w):
        me = self.Get(x, y)
        N = self.Get(x, y - 1)
        W = self.Get(x - 1, y)
        E = self.Get(x + 1, y)
        S = self.Get(x, y + 1)
        lower = me
        if S != None and S.alt <= lower.alt:
          lower = S
        if E != None and E.alt <= lower.alt:
          lower = E
        if W != None and W.alt <= lower.alt:
          lower = W
        if N != None and N.alt <= lower.alt:
          lower = N

        if lower == me or lower.alt == me.alt:
          me.next = None
        else:
          me.next = lower

  def DetermineLabel(self, n):
    if n.label != None:
      return n.label
    if n.next == None:
      n.label = chr(ord('a') + self.label_offset)
      self.label_offset += 1
    else:
      n.label = self.DetermineLabel(n.next)
    return n.label

  def Output(self):
    for y in xrange(0, self.h):
      for x in xrange(0, self.w):
        print self.DetermineLabel(self.Get(x, y)),
      print

T = int(sys.stdin.readline().strip())

for i in xrange(0, T):
  m = Map()
  m.LinkToLower()
  print "Case #%d:" % (i + 1)
  m.Output()
