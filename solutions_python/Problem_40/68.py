#!/usr/bin/env python
import re

def spaceCollapse(string):
  while string.find("  ") != -1:
    string = string.replace("  ", " ")
  string = string.replace("( ", "(")
  string = string.replace(" )", ")")
  string = string.replace(" (", "(")
  string = string.replace(") ", ")")
  return string
  
def solve(decisionTree, animal):
  animal = animal.split(' ')
  animal = animal[2:]
  p = 1.0
  i = 0
  while i<len(decisionTree):
    if(decisionTree[i] == '('):
      ws = i + 1
      while decisionTree[i] != ' ' and decisionTree[i] != ')':
        i+=1
      we = i
      weight = float(decisionTree[ws:we])
      p *= weight
      if decisionTree[i] == ' ':
        i += 1
        fs = i
        while decisionTree[i] != '(':
          i += 1
        fe = i
        feature = decisionTree[fs:fe]
        if feature in animal:
          pass
        else:
          braceCount = 1
          i += 2
          while braceCount > 0:
            if decisionTree[i] == '(':
              braceCount += 1
            elif decisionTree[i] == ')':
              braceCount -= 1
            i += 1
      else:
        print "%0.07f" % p
        return
  

N = int(raw_input())
for i in range(N):
  print "Case #%d:" % (i+1)
  count = int(raw_input())
  decisionTree = ""
  for j in range(count):
    decisionTree += raw_input()
  decisionTree = spaceCollapse(decisionTree)
  count = int(raw_input())
  animals = []
  for j in range(count):
    animals += [raw_input()]
  for animal in animals:
    solve(decisionTree, animal)
