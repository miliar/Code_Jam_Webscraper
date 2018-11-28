'''
Created on Apr 14, 2012

@author: namnx
'''
import sys

def solve(line):
    vals = line.split()
    n = int(vals[0])
    s = int(vals[1])
    p = int(vals[2])
    re = 0
    for val in vals[3:]:
        val = int(val)
        if p==1:
            if val>=1: re += 1
        elif val >= 3*p-2: re += 1
        elif val >= 3*p-4 and s > 0:
            re += 1
            s -= 1
    return re
    

if __name__ == '__main__':
    f = open(sys.argv[1])
    t = int(f.readline().strip())
    for i in xrange(t):
        line = f.readline().strip()
        re = solve(line)
        print 'Case #' + str(i+1) + ': ' + str(re)
    f.close()