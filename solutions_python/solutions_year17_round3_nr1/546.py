import sys
from StringIO import StringIO


def main():
    infile = sys.stdin
#     infile = StringIO(input)
    T = int(next(infile))
    for case_no in xrange(1, T+1):
        N, K = map(int, next(infile).strip().split(' '))
        data = []
        for i in xrange(N):
            data.append( tuple(map(int, next(infile).strip().split(' '))) )
            # R,H
        ret = solve (data, K)
        print 'Case #%d: %s' % (case_no, "{0:.6f}".format(ret))
   
def solve (data, k):
    from math import pi
    data.sort(reverse=1)
    ret = 0.0
    for j in xrange(len(data)-k+1):
        rad = data[j][0]
        side = 2.0 * pi * data[j][0] * data[j][1]
        res = solve1(data[j+1:], k-1)
        ret = max(ret, side + res + pi*rad*rad)
    return ret

def solve1 (data, k):
    from math import pi
    side = 0
    data.sort(key=lambda x: 1.0*x[0]*x[1], reverse=1)
    for i in xrange(k):
        side += 2.0 * pi * data[i][0] * data[i][1]
    return side 


if __name__ == '__main__':
    main()
