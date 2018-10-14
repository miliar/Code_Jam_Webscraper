import sys
import math
#import itertools

debug = False

def read_case(lines):
    n,A,B,C,D,x0,y0,M = [int(e) for e in lines[0].strip().split()]
    return list(get_trees(n,A,B,C,D,x0,y0,M)), lines[1:]

def get_trees(n,A,B,C,D,x0,y0,M):
    x,y = x0,y0
    yield (float(x),float(y))
    if debug : print 'Tree at', x,y
    for i in xrange(n-1):
        x = (A * x + B) % M
        y = (C * y + D) % M
        if debug : print 'Tree at', x,y
        yield (float(x),float(y))

def process_case(c_data):
    result = 0
    for x1,y1 in c_data:
        for x2,y2 in c_data:
            for x3,y3 in c_data:
                if ((x1,y1) != (x2,y2) and (x2,y2) != (x3,y3) and (x1,y1) != (x3,y3)) :
                    if debug : print 'triangle:',x1,y1,x2,y2,x3,y3
                    if debug : print 'Center at', (x1 + x2 + x3) / 3.0, (y1 + y2 + y3) / 3.0
                    if (int((x1 + x2 + x3) / 3.0), int((y1 + y2 + y3) / 3.0)) == (((x1 + x2 + x3) / 3.0), ((y1 + y2 + y3) / 3.0)) :
                        result += 1
    return result/6

def interpretate(result):
    #response = ''
    response = str(result)
    return response

if __name__ == '__main__':
    case = 0
    lines = open(sys.argv[1]).readlines()[1:]
    while(lines != []):
        c_data, lines = read_case(lines)
        case += 1
        print 'Case #%d:' % case, interpretate(process_case(c_data))
