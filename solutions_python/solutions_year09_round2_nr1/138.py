#!/usr/bin/env python
import sys
import re
sys.setrecursionlimit(10000)

terms = []

def main():
  global terms
  
  N = int(sys.stdin.readline().strip())

  for case in range(1, N + 1):
    L =  int(sys.stdin.readline().strip())

    string = ''
    for l in range(L):
      string += sys.stdin.readline()
    string = re.sub(r'\n', ' ', string)
    string = re.sub(r'\)', ' ) ', string)
    string = re.sub(r'\(', ' ( ', string)
    terms = filter(lambda x:x, re.split(r'\s+', string))

    root = build_tree(0, len(terms) - 1)
      
    A = int(sys.stdin.readline().strip())

    print 'Case #' + str(case) + ':'    
    for a in range(A):
      animal = sys.stdin.readline().strip().split(' ')
      features = set(animal[2:])
      prob = 1.0
      print '%.6f' % root.prob(features)





def build_tree(s, e):
  global terms
  
  if (e - s == 2):
    leaf = Node()
    leaf.weight = float(terms[s + 1])
    return leaf

  root = Node()
  root.weight = float(terms[s + 1])
  root.feature = terms[s + 2]

  para = 1
  i = s + 4
  while para > 0:
    if terms[i] == '(':
      para += 1
    elif terms[i] == ')':
      para -= 1
    i += 1
  
  root.sub.append(build_tree(s + 3, i - 1))
  root.sub.append(build_tree(i , e - 1))
  return root
  

class Node:

  def __init__(self):
    self.weight = .0
    self.feature = ''
    self.sub = []

  def prob(self, features):
    if len(self.sub) == 0:
      return self.weight

    if self.feature in features:
      return self.weight * self.sub[0].prob(features)
    else:
      return self.weight * self.sub[1].prob(features)



if __name__ == '__main__':
  main()
