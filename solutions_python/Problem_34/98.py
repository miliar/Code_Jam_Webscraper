#!/usr/bin/env python

#Generic libraries for the framework:
import sys
import os

#Any libraries used specifically for this problem:
import re

def solve(input, output):
  [L, D, N] = map(int, input.next().split())
  dictionary = []
  for i in range(0,D):
    dictionary.append(input.next().strip())
  for i in range(1,N+1):
    case = '^' + input.next().strip().replace('(','[').replace(')',']') + '$'
    output.write('Case #%d: %d\n' % \
        (i, reduce(lambda i,w : i + (1 if re.search(case, w) != None else 0), dictionary, 0)))


def genlines(file):
  """
  Generator to read a file stripping excessive
  whitespace and only returning non empty lines
  """
  for line in file:
    line = ' '.join(line.split())
    if (line != ''):
      yield line

def checkresult(result, check):
  """
  Compare result to a provided answer ignoring
  excessive whitespace and empty lines
  """
  resultlines = genlines(result)
  checklines  = genlines(check)
  for rline in resultlines:
    try:
      cline = checklines.next()
    except:
      print ">>> Result too large, this line was extra:"
      print "   ", rline
      break
    if rline != cline:
      print "X!     result:", rline
      print " !> should be:", cline
  try:
    cline = checklines.next()
    print "<<< Result too small, missing this line:"
    print "   ", cline
  except: pass

def usage():
  print sys.argv[0] + " in out [test]"

def main():
  """
  Framework for processing and
  checking Google's Code Jam problems
  """
  if not 2 < len(sys.argv) < 5:
    usage()
    return
  checkanswer = len(sys.argv) == 4

  if os.path.exists(sys.argv[2]):
    print sys.argv[2] + " exists, overwrite?"
    if sys.stdin.readline().strip().lower()[0] != 'y':
      return

  input  = open(sys.argv[1], 'rb')
  output = open(sys.argv[2], 'wb')
  if checkanswer:
    check = open(sys.argv[3], 'rb')

  solve(input, output)

  if checkanswer:
    print "Checking result..."
    output.close()
    output = open(sys.argv[2], 'rb')
    checkresult(output, check)
    print "Done"
  else:
    print "Not checking result"

if __name__ == '__main__':
  main();
