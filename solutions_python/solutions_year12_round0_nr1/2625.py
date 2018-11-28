#! /usr/bin/python

import sys
from collections import deque

def solve(line):
    out = ''
    abc = {'y':'a','n':'b','f':'c',
           'i':'d','c':'e','w':'f',
           'l':'g','b':'h','k':'i',
           'u':'j','o':'k','m':'l',
           'x':'m','s':'n','e':'o',
           'v':'p','z':'q','p':'r',
           'd':'s','r':'t','j':'u',
           'g':'v','t':'w','h':'x',
           'a':'y','q':'z'}
    for letter in line:
        if letter == ' ':
            out += letter
        else:
            out += abc[letter]
    return out

lines = deque()
with open(sys.argv[1],'r') as f:
    for line in f: lines.append(line.strip())

casesLength = lines.popleft()
casesLength = int(casesLength)

sys.stdout = open('result','w')
casekey = 1
for case in lines:
    print "Case #{0}: {1}".format(casekey,solve(case))
    casekey = casekey + 1
