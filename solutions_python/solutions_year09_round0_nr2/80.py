#!/usr/bin/env python

#Generic libraries for the framework:
import sys
import os

#Any libraries used specifically for this problem:

def minelevation(elevation, x,y):
  """
  Find the minimum elevation from a cell and it's neighbours
  """
  (e,r) = elevation[y][x]
  (nx,ny) = (x,y)
  for (i,j) in [(x,y-1),(x-1,y),(x+1,y),(x,y+1)]:
    if (i >= 0 and j >= 0):
      try:
        (ne, nr) = elevation[j][i]
        if (ne < e): (nx,ny, e,r) = (i,j, ne,nr)
      except: pass #border conditions
  return (nx,ny, e,r)

def solve(input, output):
  T = int(input.next().strip())
  #print T
  for t in range(1,T+1):
    [H,W] = map(int, input.next().split())
    #print W,H
    elevation = []
    for h in range(0,H):
      elevation.append(map(lambda e:(int(e),''), input.next().split()))
    #print elevation
    nextsinc = 'a'
    for y in range(0,H):
      for x in range(0,W):
        #print 'processing %i,%i' % (x,y)
        flow = [(x,y)]
        for (i,j) in flow:
          #print 'flowed to %i,%i' % (i,j)
          (e,r) = elevation[j][i]
          (nx,ny, ne,nr) = minelevation(elevation, i,j)
          if nr != '':
            pass
            #print 'flow found existing basin %s at %i,%i' % (nr, nx, ny)
          elif e != ne:
            flow.append((nx,ny))
          else: #sinc
            nr = nextsinc
            #print 'found sinc %s at %ix%i' % (nr, nx,ny)
            nextsinc = chr(ord(nextsinc)+1)
        for (i,j) in flow:
          (e,r) = elevation[j][i]
          elevation[j][i] = (e,nr)
    output.write('Case #%d:\n' % t)
    for y in range(0,H):
      for x in range(0,W):
        (e,r) = elevation[y][x]
        output.write(r + ' ')
      output.write('\n')

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
