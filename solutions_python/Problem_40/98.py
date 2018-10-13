#!/usr/bin/env python
# encoding: utf-8
"""
AlienLanguage.py

Created by Graham Dennis on 2009-09-03.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import re
import sys
import getopt


help_message = '''
The help message goes here.
'''


class Usage(Exception):
  def __init__(self, msg):
    self.msg = msg


class Node(object):
  __slots__ = ['weight', 'name', 'true', 'false']
  def __init__(self, weight = 1.0):
    self.weight = weight
    self.name = None
    self.true = None
    self.false = None

def traverse(root, qualities):
  result = root.weight
  if root.name is not None:
    if root.name in qualities:
      result *= traverse(root.true, qualities)
    else:
      result *= traverse(root.false, qualities)
  return result



def main(argv=None):
  if argv is None:
    argv = sys.argv
  try:
    try:
      opts, args = getopt.getopt(argv[1:], "ho:v", ["help", "output="])
    except getopt.error, msg:
      raise Usage(msg)
    
    # option processing
    for option, value in opts:
      if option == "-v":
        verbose = True
      if option in ("-h", "--help"):
        raise Usage(help_message)
      if option in ("-o", "--output"):
        output = value
  
  except Usage, err:
    print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
    print >> sys.stderr, "\t for help use --help"
    return 2
  
  f = file(args[0])
  N = int(f.readline())
  regex = re.compile(r'([()]|\d\.\d+|\w+)')
  for n in xrange(N):
    L = int(f.readline())
    text = ''.join(f.readline() for _ in xrange(L))
    tokens = tuple(regex.findall(text))
    
    def parse(tokenIdx):
      state = True
      assert tokens[tokenIdx] == '(', "token was '%s'" % tokens[tokenIdx]
      tokenIdx += 1
      child = Node(float(tokens[tokenIdx]))
      
      tokenIdx += 1
      if not tokens[tokenIdx] == ')':
        child.name = tokens[tokenIdx]
        tokenIdx += 1
        child.true, tokenIdx = parse(tokenIdx)
        child.false, tokenIdx = parse(tokenIdx)
      assert tokens[tokenIdx] == ')', "token was '%s'" % tokens[tokenIdx]
      tokenIdx += 1
      return child, tokenIdx
    
    root, tokenIdx = parse(0)
    
    print "Case #%i:" % (n+1)
    
    A = int(f.readline())
    for a in xrange(A):
      qualities = set(f.readline().split()[2:])
      result = traverse(root, qualities)
      print "%(result).7f" % locals()
    
  


if __name__ == "__main__":
  sys.exit(main())
