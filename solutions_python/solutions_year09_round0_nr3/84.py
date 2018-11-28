#!/usr/bin/env python

#Generic libraries for the framework:
import sys
import os

#Any libraries used specifically for this problem:

search = "welcome to code jam"
sol = {}

def solveintermediate(s, strloc, searchloc):
  #print 'searching for (%i,%i) "%s" in "%s"' % (searchloc,strloc,search[searchloc:], s[strloc:])
  if len(search[searchloc:]) > len(s[strloc:]):
    #print 'string too long'
    return 0
  prev = sol.get((strloc, searchloc))
  if prev != None:
    #print 'previous solution to (%i,%i): %i' % (strloc,searchloc,prev)
    return prev
  loc = s.find(search[searchloc], strloc) + 1
  if (loc == 0):
    ret = 0
  elif searchloc == len(search)-1:
    ret = 1
    ret += solveintermediate(s, loc, searchloc);
  elif loc < len(s):
    ret  = solveintermediate(s, loc, searchloc);
    ret += solveintermediate(s, loc, searchloc+1);
  else:
    ret = 0
  #print 'saving solution to (%i,%i): %i ("%s" in "%s")' % (strloc,searchloc,ret,search[searchloc:], s[strloc:])
  sol[(strloc, searchloc)] = ret
  return ret


def solve(input, output):
  global sol
  T = int(input.next().strip())
  for t in range(1,T+1):
    s = input.next().strip()
    sol = {} #hashmap to store intermediate solutions
    n = solveintermediate(s, 0, 0)
    output.write('Case #%d: %.4d\n' % (t, n % 10000))
    output.flush()

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
