from __future__ import division
from fractions import gcd
import numpy

def rins():
    return raw_input().strip()

def calc_stuff(row, k):
    cvn = numpy.array(range(1-k, k, 2))
    return numpy.convolve(row, cvn, 'valid')

def make_kgrids(grid):
    r,c = grid.shape
    max_k = min(r,c)
    kgrids={}
    for k in xrange(max_k,0,-1):
        kgrids[k] = numpy.zeros((r, c-k+1), dtype=numpy.int64)
        for rr in xrange(r):
            kgrids[k][rr,:] = calc_stuff(grid[rr,:],k)
    return kgrids

def solve_next():
    r,c,d = [int(ch) for ch in rins().split()]
    grid = numpy.array([
        [int(ch) for ch in rins()]
        for i in xrange(r)
        ])
    grid[:,:] += d
    max_k = min(r,c)
    kgrids=make_kgrids(grid)
    fkgrids=make_kgrids(numpy.transpose(grid))
    for k in xrange(max_k,0,-1):
        kgrids[k] = numpy.zeros((r, c-k+1), dtype=numpy.int64)
        for rr in xrange(r):
            kgrids[k][rr,:] = calc_stuff(grid[rr,:],k)
        #print k
        #print kgrids[k]
    #print max_k
    for k in xrange(max_k,2,-1):
        ogrid = numpy.zeros((r-k+1,c-k+1),dtype=numpy.int64)
        cvn = numpy.array(range(3-k, k-2, 2))
        #print cvn
        for top_row in xrange(r-k+1):
            bottom_row = top_row+k-1
            for left_col in xrange(c-k+1):
                lesser_k = k - 2
                top_v = kgrids[lesser_k][top_row,left_col+1]
                bottom_v = kgrids[lesser_k][bottom_row,left_col+1]
                other_v = numpy.sum(kgrids[k][top_row+1:bottom_row,left_col])
                v = top_v + bottom_v + other_v
                right_col = left_col + k - 1
                top_w = fkgrids[lesser_k][left_col,top_row+1]
                bottom_w = fkgrids[lesser_k][right_col,top_row+1]
                other_w = numpy.sum(fkgrids[k][left_col+1:right_col,top_row])
                w = top_w + bottom_w + other_w


                ogrid[top_row,left_col]=v
                #if top_row==1 and left_col==1:
                #    print v,w
                #    print "k=%s, top_v=%s, bottom_v=%s, other_v=%s" % (k, top_v, bottom_v, other_v)
                #    print kgrids[k][top_row+1:bottom_row,left_col]
                #    print cvn
                #    print cvn * kgrids[k][top_row+1:bottom_row,left_col]
                if v==0 and w==0:
                    #print top_row, left_col
                    return k
        #print ogrid
    return "IMPOSSIBLE"

def run():
    t = int(rins())
    for i in xrange(t):
        print "Case #{0}: {1}".format(i+1, solve_next())

run()
