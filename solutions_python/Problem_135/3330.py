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
  
  with open(sys.argv[1], 'r') as f:

    test_cases = int(f.readline())
    for i in range(test_cases):
      # Read guess 1
      m1 = []
      guess1 = int(f.readline())
      m1.append(map(int, f.readline().split()))
      m1.append(map(int, f.readline().split()))
      m1.append(map(int, f.readline().split()))
      m1.append(map(int, f.readline().split()))

      m2 = []
      guess2 = int(f.readline())
      m2.append(map(int, f.readline().split()))
      m2.append(map(int, f.readline().split()))
      m2.append(map(int, f.readline().split()))
      m2.append(map(int, f.readline().split()))

      answer = set(m1[guess1-1]) & set(m2[guess2-1])

      msg = ''
      if len(answer) == 0:
        msg = "Volunteer cheated!"
      elif len(answer) > 1:
        msg = "Bad magician!"
      else:
        msg = answer.pop()
      print 'Case #%d: %s' % ((i+1), msg)
