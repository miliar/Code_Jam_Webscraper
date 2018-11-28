#!/usr/bin/env python
import pprint as pp

def read():
    line = raw_input().strip()
    R,C = [int(i) for i in line.split()]
    data = []
    for i in xrange(R):
        data.append( [c for c in raw_input().strip()[:C]] )
    return R, C, data

def next(t0,p0,p,to):
    t = max(t0 + abs(p-p0)+1, to+1)
    return t, p

def make_red(data, i, j, R, C ):
    if i+1>=R or j+1 >=C: return False
    try:
        if data[i][j] == '#': data[i][j] = '/'
        else: return False
        if data[i][j+1] == '#': data[i][j+1] = '\\'
        else: return False
        if data[i+1][j] == '#': data[i+1][j] = '\\'
        else: return False
        if data[i+1][j+1] == '#': data[i+1][j+1] = '/'
        else: return False
        return True
    except:
        return False

def run_test():
    R, C, data = read()
    #print R, C, data
    for i in xrange(R):
        for j in xrange(C):
            if data[i][j]=='#': # blue
                if make_red(data, i, j, R, C)==False:
                    return 'Impossible'
                #else: print i, j, True
    return '\n'.join([''.join(d) for d in data])

def main():
    tests = int(raw_input())
    for test in xrange(tests):
        print "Case #%i:\n%s"%(test+1, str(run_test()))

main();
