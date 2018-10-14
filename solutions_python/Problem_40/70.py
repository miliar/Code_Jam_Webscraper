#!/usr/bin/python

import sys
import string
import logging
import time

import re

TOKENS = "left", "weight", "feature", "right"

LEFT=re.compile("^\(")
RIGHT=re.compile("^\)")
FEATURE=re.compile("^[a-z]+")
WHITESPACE=re.compile("^\s+")
WEIGHT=re.compile("^[0-9.]+")

def tokenize(str):
  tokens = []
  while(str):
    m = WHITESPACE.match(str)
    if m:
      str = str[m.end():]
      continue
    for r, s in zip([LEFT, WEIGHT, FEATURE, RIGHT], TOKENS):
      m = r.match(str)
      if m:
        tokens.append( (s, m.group()) )
        str = str[m.end():]
        break
  logging.info(tokens)
  return tokens

def make_trees(tokens):
  # logging.info(tokens)
  if not tokens:
    assert False

  cur = tokens.pop(0)
  assert cur[0] == "left"
  w, weight = tokens.pop(0)
  assert w == "weight"
  weight = float(weight)
  cur = tokens.pop(0)
  if cur[0] == "right":
    return Tree(weight=weight)
  else:
    f, feature = cur
    assert f == "feature"
    left = make_trees(tokens)
    right = make_trees(tokens)
    cur = tokens.pop(0)
    assert cur[0] == "right"
    return Tree(weight=weight, feature=feature, left=left, right=right)

def parse(input):
  tokens = tokenize(input)
  return make_trees(tokens)

class Tree(object):
  def __init__(self, weight, feature=None, left=None, right=None):
    self.weight=weight
    self.feature=feature
    self.left=left
    self.right=right

  def __str__(self):
    return "Tree(%s, %s, %s, %s)" % (self.weight, self.feature, self.left, self.right)



if __name__ == "__main__":
  logging.basicConfig(level=logging.INFO)
  input = file(sys.argv[1])
  num_problems = int(input.readline().strip())
  for i in range(num_problems):
    print "Case #%d:" % (i+1)
    input_lines = int(input.readline().strip())
    tree = " ".join([ input.readline() for _ in range(input_lines)]).replace("\n", " ")
    logging.info(tree)
    parsed = parse(tree)
    logging.info(parsed)

    num_animals = int(input.readline().strip())
    for j in range(num_animals):
      features = input.readline().strip().split(" ")[2:]
      features = set(features)

      prob = 1.0
      cur_tree = parsed
      while cur_tree:
        prob *= cur_tree.weight
        if cur_tree.feature:
          if cur_tree.feature in features:
            cur_tree = cur_tree.left
          else:
            cur_tree = cur_tree.right
        else:
          cur_tree = None

      print "%f" % prob
