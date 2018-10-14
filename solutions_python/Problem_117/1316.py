import collections
from collections import Counter
import pdb
import sys

def arePathsClear(s, lawn, N, M):
  #print >> sys.stderr, "arePathsClear(%s,%s,%s,%s)" % (str(s), str(lawn), str(N), str(M))
  isClearRows = True
  isClearCols = True
  val = lawn[s]

  for r in range(0,N):
    isClearRows &= val >= lawn[(r,s[1])]
    #print >> sys.stderr, '(%d,%d)'%(r,s[1]), val, lawn[(r,s[1])], val >= lawn[(r,s[1])], isClearRows, 'r'

  for c in range(0,M):
    isClearCols &= val >= lawn[(s[0],c)]
    #print >> sys.stderr, '(%d,%d)'%(s[0],c), val, lawn[(s[0],c)], val >= lawn[(s[0],c)], isClearCols, 'c'
  
  #print >> sys.stderr, "isClearRows or isClearCols", isClearRows or isClearCols
  return isClearRows or isClearCols


if __name__ == '__main__':
  
  f = open(sys.argv[1], 'r')

  test_cases = int(f.readline())
  for i in range(test_cases):
    N,M = map(int, f.readline().split())
    lawn = dict([])
    for row in range(N):
      for col,val in enumerate(map(int,f.readline().split())):
        lawn[(row,col)] = val

    sorted_squares = sorted(lawn,
                            key=lambda x: lawn[x])
    # Start from the smallest item
    # make sure there is a clear path
    # meaning no greater values up, down, left 
    # and right.
    isClear = True
    for s in sorted_squares:
      isClear &= arePathsClear(s, lawn, N, M) 

    msg = 'YES' if isClear else 'NO'
    print 'Case #%d: %s' % ((i+1), msg)
    #print >> sys.stderr, '-'*80
  f.close()
