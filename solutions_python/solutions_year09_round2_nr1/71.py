#!/usr/bin/env python
# Marco Gallotta
import math, sys, re

def construct_tree(input):
  input = input.strip()
  assert input[0] == '('
  assert input[-1] == ')'
  input = input[1:-1].strip()
  space = input.find(" ")
  if space == -1:
    return (float(input), None)
  p = input[:space]
  input = input[space+1:]
  space = input.find(" ")
  assert space != -1
  feature = input[:space]
  input = input[space+1:].strip()
  brackets = 1
  for i in xrange(1, len(input)):
    if input[i] == "(":
      brackets += 1
    elif input[i] == ")":
      brackets -= 1
      if brackets == 0:
        break
  left, right = input[:i+1], input[i+1:]
  return (float(p), feature, construct_tree(left), construct_tree(right))

def solve(tree, features):
  p = tree[0]
  if tree[1] != None:
    if tree[1] in features:
      p *= solve(tree[2], features)
    else:
      p *= solve(tree[3], features)
  return p

T = int(raw_input())
for case in xrange(1, T+1):
  print "Case #%d:" % case
  L = int(raw_input())
  tree_input = " ".join([raw_input() for line in xrange(L)])
  tree = construct_tree(tree_input)
  A = int(raw_input())
  for a in xrange(A):
    line = raw_input().split()
    animal = line[0]
    n = int(line[1])
    features = set(line[2:])
    print "%.8f" % solve(tree, features)
