#!/usr/bin/python
import re
#import logging

FILE='A-small-attempt1'

# logging.basicConfig(level = logging.DEBUG, 
#                    format = '%(message)s',
#                    filename = FILE + '.log',
#                    filemode = 'w')

def isinvocab(word):
    for a in vocab:
        if a.find(word) != -1:
            return 1
    return 0

def solve(case, word):
    #logging.debug("To process: " + case)
    #logging.debug("Word: " + word)
    # Treat final case
    if not case:
        if (word in vocab):
            #logging.debug("found")
            return 1
        else:
            #logging.debug("not found")
            return 0
    # Get next match
    res = re.match('[a-z]|\([a-z]+\)', case).group()
    next = len(res)
    # Strip parenthesis if needed
    if (res.find('(') != -1):
        res = res[1:len(res)-1]
    # For each letter, invoke recursively
    ret = 0;
    for letter in res:
        newword = word+letter
        if isinvocab(newword):
            ret = ret + solve(case[next:len(case)], newword)
    return ret

# Input
fin = open(FILE + '.in', 'r')
fout = open(FILE + '.out', 'w')

opt = fin.readline().split()
L = int(opt[0]) # Word size
D = int(opt[1]) # Number of words
N = int(opt[2]) # Number of cases
#logging.debug("Word size - L: " + str(L))
#logging.debug("Number of words - D: " + str(D))
#logging.debug("Number of cases - N: " + str(N))

vocab = []
for i in range(D):
    vocab.append(fin.readline().strip('\n'))
#logging.debug("Vocabulary: " + str(vocab))

cases = []
for i in range(N):
    cases.append(fin.readline().strip('\n'))
#logging.debug("Cases: " + str(cases))

# Treat cases
for casenum, case in enumerate(cases):
    sol = solve(case, "")
    msg = "Case #" + str(casenum+1) + ": " + str(sol)
    print msg
    fout.write(msg+'\n')