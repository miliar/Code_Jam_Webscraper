# -*- coding:utf-8 -*-
import os, math, cmath
from operator import itemgetter

curr_dir = os.path.dirname(os.path.abspath(__file__))
srcfilename = os.path.join(curr_dir, 'B-large.in')
dstfilename = os.path.join(curr_dir, 'B-large.out.txt')

def solve(width, height, rs):
#    import ipdb; ipdb.set_trace()
    rs_i = list(enumerate(rs))
    rs_i.sort(key = itemgetter(1), reverse=True)
    x = y = 0
    points = {}
    radiuses = {}
    for index, ri in enumerate(rs_i):
        radiuses[index] = ri[1]
    
    for index, ri in enumerate(rs_i):
        orig_index, r = ri
        if index == 0:
            rprev = r
        nextr = radiuses[index+1] if index+1 in radiuses else 0
        points[orig_index] = (x, y)
        x += r + nextr
        if x > width:
            x = 0
            y += rprev + nextr
            rprev = r
        
    results = []
    for orig_index in xrange(len(rs)):
        results += list(points[orig_index])
    return results
        

if __name__ == '__main__':
    with open(srcfilename, 'rb') as inp:
        with open(dstfilename, 'wb') as outp:
            count = int(inp.readline())
            for i in xrange(count):
                N, W, L = [int(number) for number in inp.readline().split(' ')]
                rs = [int(number) for number in inp.readline().split(' ')]
                results = solve(W, L, rs)
                outline = 'Case #%d: %s\n' % (i+1, ' '.join(['%d' % result for result in results]))
                outp.writelines([outline])
                outp.flush()
