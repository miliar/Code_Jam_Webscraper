'''
Created on 3 may 2014

@author: algestam
'''

def handle(a, b, k):
    wins = 0
    for va in range(a):
        for vb in range(b):
            if va&vb < k:
                wins += 1
    return wins

for case in xrange(input()):
    a, b, k = [int(v) for v in raw_input().split()]
    res = handle(a, b, k)
    print "Case #%i: %s" % (case+1, res)