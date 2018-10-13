#!/usr/bin/env python
import sys
import numpy as np
sys.setrecursionlimit(2000)
def get_result(pattern, K):
    # print pattern, K
    if (pattern==1).all():
        return 0
    if (len(pattern)<K):
        return "IMPOSSIBLE"
    if (len(pattern)==K):
        if (pattern==0).all():
            # print "1, flip"
            return 1
        else:
            return "IMPOSSIBLE"
    lastindex = np.max(np.where(pattern==0)[0])
    firstindex = np.min(np.where(pattern==0)[0])
    if not firstindex ==0 or not lastindex==(len(pattern)-1):
        return get_result(pattern[firstindex:lastindex+1], K)
    pattern[:K] = 1-pattern[:K]
    result = get_result(pattern[1:],K)
    if result== "IMPOSSIBLE":
        return "IMPOSSIBLE"
    else:
        # print "2, flip"
        return 1+result

def test():
    pattern = np.random.randint(2, size=10)
    K = np.random.randint(2, high=10)
    print pattern, K
    print get_result(pattern, K)
    return 

if __name__=='__main__':
    infile = sys.argv[1]
    fin = open(infile,mode='r')
    Ncase = int(fin.readline().rstrip())
    def func(x):
        return x=='+'
    for i in xrange(Ncase):
        line = fin.readline().rstrip()
        pattern = map(func, [x for x in line.split()[0]])
        result = get_result(np.array(pattern).astype(int), int(line.split()[1]))
        print "Case #%d: %s" % (i+1, result)



