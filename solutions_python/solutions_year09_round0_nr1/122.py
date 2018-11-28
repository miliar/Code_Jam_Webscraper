import re
from itertools import izip

def check(dw, w):
    for dwi, wi in izip(dw, w):
        if dwi not in wi:
            return False
    return True

def main(infn):
    inf = open(infn)
    l, d, n = [int(x) for x in inf.readline().split()]
    dic = []
    for i in range(d):
        dic.append(inf.readline().strip())

    for i in range(n):
        w = inf.readline().strip()
        m = re.findall('\((\w+)\)|(\w)', w)
        w = [x[0] if x[0] else x[1] for x in m]
        
        count=0
        for dw in dic:
            if check(dw, w):
                count+=1

        print 'Case #%d: %d'%(i+1, count)
    return

import sys
main(*sys.argv[1:])


