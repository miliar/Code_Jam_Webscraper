#!/usr/bin/env python
# encoding: utf-8
"""
TheNextNumber.py

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
  T = int(f.readline())
  for t in xrange(T):
    line = f.readline().strip()
    N = ['0'] + list(line)
    start = len(N) - 2
    while start >= 0:
      if N[start] < N[start + 1]:
        N[start], N[start+1] = N[start + 1], N[start]
        M = N[start:]
        M.sort()
        # print line, N, N[start], M
        firstDigit = min(m for m in M if m > N[start+1])
        M.remove(firstDigit)
        N = N[:start] + [firstDigit] + M
        break
      start -= 1
    assert start >= 0, "old: %s, new: %s" % (line, ''.join(N))
    while N[0] == '0': N.pop(0)
    assert long(line) < long(''.join(N)), "old: %s, new: %s" % (line, ''.join(N))
    print "Case #%i: %s" % (t + 1, ''.join(N))
    # print "Case #%i: %s %s" % (t + 1, line, ''.join(N))
    
  


if __name__ == "__main__":
  sys.exit(main())
