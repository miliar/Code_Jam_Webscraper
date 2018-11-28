'''
Created on Apr 15, 2012

@author: namnx
'''
import sys

def solve(line):
    vals = line.strip().split()
    a = int(vals[0])
    b = int(vals[1])
    re = 0
    for val in xrange(a,b+1):
        sval = str(val)
        valid_vals = set()
        for i in xrange(len(sval)-1):
            new_val = sval[-(i+1):] + sval[:-(i+1)]
            if new_val[0] == '0': continue
            new_val = int(new_val)
            if new_val <= val: continue
            if new_val >= a and new_val <=b:
                valid_vals.add(new_val)
        re += len(valid_vals)
    return re


if __name__ == '__main__':
    f = open(sys.argv[1])
    t = int(f.readline().strip())
    for i in xrange(t):
        re = solve(f.readline().strip())
        print 'Case #' + str(i+1) + ': ' + str(re)
    f.close()