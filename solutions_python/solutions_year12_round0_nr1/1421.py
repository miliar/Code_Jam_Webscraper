from sys import *

def solve(_, words):
    x = 'abcdefghijklmnopqrstuvwxyz '
    y = 'ynficwlbkuomxsevzpdrjgthaq '
    out = ''
    print "Case #%d:" %(_+1),
    for i in range(0,len(words)):
        if words[i] in x:
            out += x[y.find(words[i])]  
    print out
    
cases = int(raw_input())
for _ in xrange(cases):
    words = str(raw_input())
    solve(_,words)
