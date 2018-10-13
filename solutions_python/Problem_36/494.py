from __future__ import division

global cn
cn = 1
def format(res):
    global cn
    print "Case #" +  str(cn) + ":", res
    cn += 1

import os
lines = open(os.getcwd() + '/' + "input.txt").read().split("\n")
lines = lines[1:]

phrase = 'welcome to code jam'

for line in lines:
    #line = """So you've registered. We sent you a welcoming email, to welcome you to code jam. But it's possible that you still don't feel welcomed to code jam. That's why we decided to name a problem "welcome to code jam." After solving this problem, we hope that you'll feel very welcome. Very welcome, that is, to code jam.After solving this problem, we hope that you'll feel very welcome. Very welcome, that is, to code jam.After solving this problem, we hope that you'll feel very welcome. Very welcome, that is, to code jam."""

    orig = line
    
    arr = []
    count = []
    d = {}
    
    
    for i in range(1, len(phrase)+1):
        arr.append(phrase[:i])
        count.append(0)
    
    for l in line:
        n = phrase.find(l)
        while n != -1:
            if n==0:
                count[n] += 1
            else:
                count[n] += count[n-1]
            n = phrase.find(l, n+1)
    format(str(count[-1]).zfill(4))
    
    

    
