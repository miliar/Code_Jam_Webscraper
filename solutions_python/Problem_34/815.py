from __future__ import division

global cn
cn = 1
def format(res):
    global cn
    print "Case #" +  str(cn) + ":", res
    cn += 1

import os
lines = open(os.getcwd() + '/' + "input.txt").read().split("\n")


important_nums = lines[0].split(" ")


wordnum = int(important_nums[1])
lines = lines[1:]


knownwords = lines [:wordnum]

dwords = {}
for word in knownwords: dwords[word] = True

lines = lines [wordnum:]


def numWords(token, wordSoFar = ""):
    found = False
    for word in knownwords:
        if word.find(wordSoFar) != -1: 
            found = True
            break
    if found == False: return 0
    
    if len(token) == 0:
        if wordSoFar in dwords:
            return 1
        return 0
    
    sum = 0
    for l in token[0]:
        sum += numWords(token[1:], wordSoFar + l)
    return sum
        
        

for word in lines:
    tokens = []
    isParen = False
    newToken = ""
    for l in word:
        if l == '(': 
            isParen = True
            continue
        if l == ')': 
            isParen = False
            tokens.append(newToken)
            newToken = ""
            continue
        if not isParen:
            tokens.append(l)
            newToken = ""
        if isParen:
            newToken += l
    format (numWords(tokens))
    #format( sum([ a[0] * a[1]  for a in zip(a1, a2)]))
    


