#!/usr/bin/env python
# encoding: utf-8
"""
AlienLanguage.py

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


def matches(lst, target):
  if not target: return 1
  result = 0
  for string, successorList in lst:
    if not string in target[0]: continue
    result += matches(successorList, target[1:])
  return result

def insertString(lst, stringToInsert):
  for string, successorList in lst:
    if stringToInsert[0] == string:
      return insertString(successorList, stringToInsert[1:])
  newList = None
  if len(stringToInsert) > 1:
    newList = []
    insertString(newList, stringToInsert[1:])
  lst.append((stringToInsert[0], newList))

root = []

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
  L, D, N = map(int, f.readline().split())
  for i in xrange(D):
    insertString(root, f.readline().strip())
  
  # print root
  
  for i in xrange(N):
    line = f.readline().strip()
    lineList = []
    state = 0
    string = ''
    for char in line:
      if char == '(': 
        state = 1
        if string: 
          lineList.extend(string)
          string = ''
      elif char == ')':
        state = 0
        lineList.append(list(string))
        string = ''
      else:
        string += char
    if string: lineList.extend(string)
    
    # print line, lineList, matches(root, lineList)
    print "Case #%i: %i" % (i + 1, matches(root, lineList))
  


if __name__ == "__main__":
  sys.exit(main())
