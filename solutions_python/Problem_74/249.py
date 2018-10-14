'''
Created on 7 maj 2011

@author: rickard
'''
import sys

def solve(seq):
    seq = seq.split()
    num = int(seq[0])
    assert 2 * num == len(seq)-1
    
    posO = posB = 1
    timO = timB = 0
    for i in range(num):
        bot = seq[2*i+1]
        btn = int(seq[2*i+2])
        assert bot in ('B','O')
        
        if bot == 'B':
            timB += abs(btn - posB)
            timB = max(timB, timO) + 1
            posB = btn
        else:
            timO += abs(btn - posO)
            timO = max(timO, timB) + 1
            posO = btn
    return max(timB, timO)

count = int(sys.stdin.readline())
for c,line in enumerate(sys.stdin):
    print "Case #%d: %d" % (c+1, solve(line))
