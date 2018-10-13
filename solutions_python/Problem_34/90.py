import re
import sys

import psyco
psyco.full()

class Node:
  def __init__(self, letter):
    self.reachable = False
    self.letter = letter
    self.next = {}

  def reach(self):
    self.reachable = True

  def count(self, word_length, depth=0):
    total = 0
    if depth == word_length:
      return 1
    for l in self.next:
      if self.next[l].reachable:
        total += self.next[l].count(word_length, depth+1)
    return total

  def reset(self):
    self.reachable = False
    [x.reset() for x in self.next.itervalues()]

  def addNode(self, letter):
    if letter in self.next:
    	return self.next[letter]
    self.next[letter] = Node(letter)
    return self.next[letter]

  def nextLetter(self, letter):
    if letter in self.next:
      return self.next[letter]
    return None

  def __repr__(self):
    return '<"%s" (%s)>' % (self.letter, self.next.keys())

if __name__=="__main__":
  input = open(sys.argv[1])
  L, D, N = [int(x) for x in input.readline().split()]
  words = []
  for i in xrange(D):
    words.append( input.readline().strip() )

  tree = Node('')
  for word in words:
    node = tree
    for i, l in enumerate(list(word)):
      node = node.addNode(l)
  
  for casenum, test in enumerate(input):
    test = test.strip()
    test = re.split("([a-z])|\(([a-z]+)\)", test)
    test = [x for x in test if x]
    old_active = [tree]
    for letters in test:
      active = []
      for l in letters:
        for n in old_active:
          if n.nextLetter(l):
            active.append(n.nextLetter(l))
      [x.reach() for x in active]
      old_active = active
    print "Case #%d: %d" % (casenum+1, tree.count(L))
    tree.reset()
