
import sys
import re

file1 = open('A-large.in','r')
file2 = open('A-large.out','w')
sys.stdin = file1
sys.stdout = file2
def getWordList2(line):
    inbr = False
    result = []
    word = ""
    for s in line:
        if s == '(':
            word = ""
            inbr = True
            continue
        if s == ')':
            inbr = False
            result.append(word)
            word = ""
            continue
        if inbr:
            word += s
        else:
            word = s
            result.append(word)
    return result

        
line = sys.stdin.readline()
ss = line.split()
L = int(ss[0])
D = int(ss[1])
N = int(ss[2])

words = {}
for i in xrange(D):
    word = sys.stdin.readline()
    words[word] = 1
    
for caseId in xrange(N):
    word = sys.stdin.readline()
    wordlist = getWordList2(word)

    cnt = 0
    for w in words:
        hasWord = True
        for i in xrange(len(w)):
            if w[i] not in wordlist[i]:
                hasWord = False
                break
        if hasWord:
            cnt += 1
    print "Case #%d: %d" % (caseId+1,cnt)
        
        
file1.close()
file2.close()


