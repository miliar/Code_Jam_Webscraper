"""
Clive Gifford's Solution to the "Alien language" problem, GCJ 2009
"""

import sys

def AddWord(node, word):
   if len(word) == 0: return 
   if not node.has_key(word[0]):
      node[word[0]] = {}    
   AddWord(node[word[0]], word[1:])
     
def NumWords(root, pattern, count):
   if len(pattern) > 0:
      if pattern[0] == '(':
         pos = pattern.find(')')
         possible = pattern[1:pos]
         pattern = pattern[pos+1:]
         for c in possible:
            if root.has_key(c):
               if len(pattern):
                  count = NumWords(root[c], pattern, count)
               else:
                  count += 1         
      else:
         if root.has_key(pattern[0]):
            if len(pattern) > 1:
               count = NumWords(root[pattern[0]], pattern[1:], count)
            else:
               count += 1         
   return count      

fin = file(sys.argv[1])
fout = file(sys.argv[2], "wt")

length,numWords,numCases = map(int,fin.readline().split())
alienDict = {}
for nWord in xrange(numWords):
   word = fin.readline().strip('\n')
   AddWord(alienDict, word)
for case in xrange(numCases):
   pattern = fin.readline().strip('\n')  
   fout.write("Case #%d: %d\n" % (case+1, NumWords(alienDict, pattern, 0)))   
   