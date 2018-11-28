


import sys
import re

file1 = open('C-large.in','r')
file2 = open('C-large.out','w')
sys.stdin = file1
sys.stdout = file2

word = 'welcome to code jam'
worddict = {}

def solve(word1, word2):
    if len(word1) < len(word2):
        return 0
    if len(word1) == 1:
        if len(word1) == len(word2):
            if word1 == word2:
                return 1
            else:
                return 0
    if len(word2) == 1:
        if len(word1) == len(word2):
            if word1 == word2:
                return 1
            else:
                return 0
    if len(word2) == 0:
        return 1
        
    if len(word1) == len(word2) and word1 == word2:
        return 1
    if len(word1) == len(word2) and len(word1) == 1 and word1 != word2:
        return 0
        
    if worddict.has_key((word1, word2)):
        return worddict[(word1, word2)]
    
    if word1[0] == word2[0]:
        worddict[(word1, word2)] = (solve(word1[1:],word2[1:]) + solve(word1[1:],word2)) % 10000
    else:
        worddict[(word1, word2)] = solve(word1[1:],word2) % 10000
    
    return worddict[(word1, word2)]


n = int(sys.stdin.readline())

for caseId in xrange(n):
    line = sys.stdin.readline().strip()
    worddict = {}
    res = solve(line,word)
    print "Case #%d: %04d" % (caseId+1,res)




file1.close()
file2.close()