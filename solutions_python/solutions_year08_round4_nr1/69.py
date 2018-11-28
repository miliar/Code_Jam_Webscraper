import sys, math
from copy import deepcopy

class inner:
  def __init__(self, g, c):
    self.g = g
    self.c = c
class leaf:
  def __init__(self, i):
    self.i = i

def evaluate(tree, i):
  if tree[i].__class__.__name__ == 'leaf':
    return (False, True)[tree[i].i]
  else:
    if tree[i].g == 1: # and
      return evaluate(tree, i*2+1) and evaluate(tree, i*2+2)
    else:
      return evaluate(tree, i*2+1) or evaluate(tree, i*2+2)

def change(tree, i):
  global V, nodes, M, success

  #print 'i', i, (M-1)/2

  if i >= (M-1)/2:
    #print evaluate(tree, 0), V
    if evaluate(tree, 0) == V:
      # calculate changes
     
      c = zip(tree[:(M-1)/2], nodes[:(M-1)/2])

      #print c
      
      changes = 0
      for (i1,i2) in c:
        if i1.g != i2.g:
          changes += 1
      success.append(changes)
  else:
    while tree[i].__class__.__name__ == 'inner' and tree[i].c != 1:
      i += 1
      #print 'i', i, (M-1)/2

    treecopy = deepcopy(tree)
    if tree[i].__class__.__name__ == 'inner' and tree[i].c == 1:

      for b in (True, False):
        treecopy[i].g = b
        change(treecopy, i+1)
    else:
      change(treecopy, i)
      
    
    

inputcases = int(sys.stdin.readline())
for caseno in range(inputcases):
  print 'Case #%d:' % (caseno+1),

  success = []
  
  (M, V) = map(int, sys.stdin.readline().split())
  V = (False,True)[V]

  #print M,V

  nodes = []
  for i in range((M-1)/2):
    (G, C) = map(int, sys.stdin.readline().split())
    nodes.append(inner(G,C))
  for i in range((M+1)/2):
    I = int(sys.stdin.readline())
    nodes.append(leaf(I))

  change(deepcopy(nodes), 0)

  if len(success) > 0:
    print min(success)
  else:
    print 'IMPOSSIBLE'

  
