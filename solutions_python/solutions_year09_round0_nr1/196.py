'''
Created on Sep 3, 2009

@author: spons
'''
import re
import string

def printres(case, res):
    print "Case #" + str(case) + ": " + str(res);

def conv(pattern):
    rp=[]
    #replace () into [] and hope it's quick enough
    for c in pattern:
        if c=='(': 
            c = '['
        elif c==')':
            c = ']'
        
        rp.append(c)
    rp = ''.join(rp)
    return rp

input = open('A-large.in')
sizes = input.readline()
sizes = string.split(sizes)
len = sizes[0]
alsize = int(sizes[1])
cases = int(sizes[2])

words = []
for i in range(alsize):
    #read word
    words.append(input.readline())
    pass



result = []
patterns = []
for i in range(cases):
    #solve case
    result.append(0)
    pattern = input.readline()
    patterns.append(re.compile(conv(pattern)))
    pass


for word in words:
    i = 0
    for pat in patterns:
        mat = pat.match(word)
        if mat != None: 
            result[i] = result[i] + 1
        i += 1
            
for i in range(cases):
    printres(i + 1, result[i])
    
