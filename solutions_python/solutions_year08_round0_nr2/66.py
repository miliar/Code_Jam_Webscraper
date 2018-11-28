#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Graham Dennis on 2008-06-18.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sys
import getopt


help_message = '''
The help message goes here.
'''


class Usage(Exception):
  def __init__(self, msg):
    self.msg = msg


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
  
  fd = file(args[0])
  
  numCases = int(fd.next())
  
  caseNum = 1
  
  print numCases
  
  for line in fd:
    nSearchEngines = int(line)
    searchEngines.clear()
    for idx in xrange(nSearchEngines):
      searchEngines[fd.next().strip()] = idx
    nQueries = int(fd.next())
    del queries[:]
    for idx in xrange(nQueries):
      queries.append(fd.next().strip())
    
    answer = doit()
    
    print "Case #%(caseNum)s: " % locals(), searchEngines, queries
    caseNum += 1

dp = []
queries = []
searchEngines = {}


def recursiveDo(position, state):
  if state in dp[position]:
    

def doit(searchEngines, queries):
  del dp[:]
  for query in queries:
    dp.append({})


if __name__ == '__main__':
    main()

