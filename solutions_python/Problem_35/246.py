"""
Clive Gifford's Solution to the "watersheds" problem, GCJ 2009
"""

import sys

sys.setrecursionlimit(10000)

def FindSink(row, col):
   global m, sinks, numSinks, s
   if s[row][col]:
      return s[row][col]
   a = m[row][col]
   diffN = a - m[row-1][col]
   diffW = a - m[row][col-1]
   diffE = a - m[row][col+1]
   diffS = a - m[row+1][col]
   diffMax = max(diffN, diffW, diffE, diffS)
   if diffMax <= 0:
      if not sinks.has_key((row, col)):
         numSinks += 1           
         sinks[(row, col)] = numSinks
      sink = sinks[(row, col)]    
   elif diffN == diffMax: 
      sink = FindSink(row-1, col)
   elif diffW == diffMax:
      sink = FindSink(row, col-1)
   elif diffE == diffMax:
      sink = FindSink(row, col+1)
   else:
      assert diffS == diffMax 
      sink = FindSink(row+1, col)
   s[row][col] = sink 
   return sink

fin = file(sys.argv[1])
fout = file(sys.argv[2], "wt")

maxAlt = 99999

numCases = int(fin.readline())
for case in xrange(numCases):
   numRows, numCols = map(int, fin.readline().split())
   m = []
   for row in xrange(numRows):   
      m.append([maxAlt] + map(int, fin.readline().split()) + [maxAlt])
      assert len(m[row]) == numCols + 2
   m.insert(0, [maxAlt] * (numCols + 2))
   m.append([maxAlt] * (numCols + 2))

   sinks = {}
   numSinks = 0

   s = []
   for row in xrange(numRows+2):   
      s.append([0] * (numCols + 2))

   for row in xrange(1, numRows+1):   
      for col in xrange(1, numCols+1):
         FindSink(row, col)
         assert s[row][col]
            
   fout.write("Case #%d:\n" % (case+1, ))   
   for row in xrange(1, numRows+1):   
      fout.write(' '.join([chr(ord('a')-1+s[row][col]) for col in xrange(1, numCols+1)]))
      fout.write('\n')
      
   print "Case #%d done" % (case+1, )   
   