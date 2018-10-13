import sys
import re
from pprint import pprint

input = sys.stdin
T=int(input.readline())

def process(data):

    for i in xrange(len(data)):
        for j in xrange(len(data[0])):
            if data[i][j] == '#':
                if j < len(data[0]) - 1 and data[i][j+1] == '#' and i < len(data)-1 and data[i+1][j] == '#' and data[i+1][j+1] == '#':
                    data[i][j] = '/'
                    data[i][j+1] = '\\'
                    data[i+1][j] = '\\'
                    data[i+1][j+1] = '/'
                else:
                    return None

    return data

for i in xrange(1,T+1):
    R, C=map(int, input.readline().split())
    data = []
    for l in xrange(R):
        data.append([x for x in input.readline().strip()])
    res = process(data)
    print "Case #%s:" % i
    if res is None:
        print "Impossible"
    else:
        for i in res:
            print ''.join(i)
