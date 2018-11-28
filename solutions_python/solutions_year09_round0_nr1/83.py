import sys

class Node:
  def __init__(self):
    self.count = 0
    self.subnodes = {}

  def AddMatch(self, s):
    if len(s) == 0:
      self.count += 1
      return

    node = self.subnodes.get(s[0])
    if node == None:
      node = Node()
      self.subnodes[s[0]] = node

    node.AddMatch(s[1:])

  def NumMatches(self, s):
    if len(s) == 0:
      return self.count

    if s[0] == '(':
      pos = s.find(')')
      letters = s[1:pos]
      s = s[pos + 1:]
    else:
      letters = s[0]
      s = s[1:]

    res = 0
    for c in letters:
      node = self.subnodes.get(c)
      if node == None:
        continue

      res = res + node.NumMatches(s)

    return res

(L, D, N) = map(lambda x: int(x), sys.stdin.readline().strip().split(" "))

root = Node()
for i in xrange(0, D):
  root.AddMatch(sys.stdin.readline().strip())

for i in xrange(0, N):
  print "Case #%d: %d" % (i + 1, root.NumMatches(sys.stdin.readline().strip()))
