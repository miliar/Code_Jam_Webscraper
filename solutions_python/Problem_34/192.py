#!/usr/bin/env python
import sys
import re

f = open('input.txt')
(L, D, N) = [int(t) for t in f.readline().split(' ')]

properWords = []

for wordNumber in range(1, D+1):
    properWords.append(f.readline().rstrip('\n'))

wordsForCase = []

for wordNumber in range(D+1, D+1+N):
    
    pattern = f.readline().replace('(','[').replace(')',']').rstrip('\n')

    count = 0
    
    regex = re.compile(pattern);
    
    for word in properWords:
        if regex.match(word) :
            count+=1
    
    wordsForCase.append(count)

for caseCount in enumerate(wordsForCase):
    print 'Case #' + str(caseCount[0]+1) + ': ', caseCount[1] 
    
f.close()