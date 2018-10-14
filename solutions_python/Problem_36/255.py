"""
Clive Gifford's Solution to the "welcome to code jam" problem, GCJ 2009
"""

import sys

def GetIndices(text):
   indices = {} 
   for n, c in enumerate(text):
      if not indices.has_key(c):
         indices[c] = [n]    
      else:   
         indices[c].append(n)   
   return indices
     
def CountWays(indices, phrase, pos = 0, last_n=-1):
   global count
   if pos < len(phrase):
      try:
         index = indices[phrase[pos]]
         for n in index[-1::-1]:
            if n > last_n:
               CountWays(indices, phrase, pos+1, n)
            else:
               break              
      except:
         print "\"%s\" not in text at all!" % phrase[pos]
   else:
      count += 1    
   return count      

phrase = "welcome to code jam"

fin = file(sys.argv[1])
fout = file(sys.argv[2], "wt")

numCases = int(fin.readline())
for case in xrange(numCases):
   text = fin.readline().strip('\n')  
   indices = GetIndices(text)
   count = 0
   CountWays(indices, phrase)
   sys.stdout.write("Case #%d: %04d\n" % (case+1, count % 10000))   
   fout.write("Case #%d: %04d\n" % (case+1, count % 10000))   
   