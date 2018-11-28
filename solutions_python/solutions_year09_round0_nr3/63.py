#!/usr/bin/env python
# encoding: utf-8
"""
WelcomeToCodeJam.py

Created by Graham Dennis on 2009-09-03.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
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
  
  f = file(args[0])
  N = int(f.readline())
  
  searchString = 'welcome to code jam'
  
  for i in xrange(N):
    line = f.readline().strip()
    lineArray = [1] * len(line)
    for char in searchString:
      lastCount = 0
      for idx in range(len(line)):
        if line[idx] == char:
          lastCount += lineArray[idx]
        lineArray[idx] = lastCount
    print "Case #%i: %04i" % (i+1, lineArray[-1] % 10000)
  


if __name__ == "__main__":
  sys.exit(main())
