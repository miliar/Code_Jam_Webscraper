#!/usr/bin/python

from sys import argv
from copy import copy

if len(argv) > 1:
  filename = argv[1]
else:
  filename = "test.in"

f = open(filename)

numCases = int(f.readline())

def findNodeValue(tree, gates, node): 
  child1 = node * 2 + 1
  child2 = node * 2 + 2
  if (tree[node] > -1): return tree[node]
  else:
    if (gates[node]): return 1 if (findNodeValue(tree, gates, child1) and (findNodeValue(tree, gates, child2))) else 0
    else: return 1 if (findNodeValue(tree, gates, child1) or (findNodeValue(tree, gates, child2))) else 0

def changeGates(tree, gates, changeableGates, goal, changes):
  sol = 0
  if (findNodeValue(tree, gates, 0) == goal): 
    solutions.append(changes)
    sol = 1
  else :
    for x in changeableGates:
      cGatesCopy = copy(changeableGates)
      cGatesCopy.remove(x)
      gatesCopy = copy(gates)
      gatesCopy[x] = 0 if gates[x] else 1
      newChanges = changeGates(tree, gatesCopy, cGatesCopy, goal, changes + 1)
      if (newChanges): solutions.append(changes + 1)
  return sol
  
for case in range(1, numCases + 1):
  output = ""
  
  leaves, rootgoal = map(lambda x:int(x), f.readline().split())
  gates = []
  changeableGates = []
  tree = []
  for x in range(0, (leaves-1)/2):
    gate = map(lambda x:int(x), f.readline().split())
    if (gate[1]): changeableGates.append(x)
    gates.append(gate[0])
    tree.append(-1)
  for x in range(0, (leaves+1)/2):
    tree.append(int(f.readline()))

  
  solutions = []
  status = changeGates(tree, gates, changeableGates, rootgoal, 0)
  solutions.sort()
  if (len(solutions)):
    output = str(solutions[0])
  else:
    output = "IMPOSSIBLE"
  #x1, y1, x2, y2, x3, y3 = map(lambda x:int(x), f.readline().split())

  print "Case #"+str(case)+": "+ output
