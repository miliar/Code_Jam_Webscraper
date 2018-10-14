#!/usr/bin/env python
#author: Chen Zhao

import os.path

finput = '/Users/chin/dev/codejam/2013/test.input'
finput = '/Users/chin/dev/codejam/2013/B-small-attempt4.in'
finput = '/Users/chin/dev/codejam/2013/B-large.in'

def good_cell(data, i, j, N, M):
    c = data[i][j]
    h_max = max(data[i])
    v_max = max(data[ii][j] for ii in range(N))
    return c>=h_max or c>=v_max


def solve(data, N, M):
    #DP will be faster, anyway
    if N<=1 or M<=1:
        return 'YES'

    for i in range(0,N):
        for j in range(0,M):
            if not good_cell(data, i, j, N, M):
                return 'NO'

    return 'YES'

def show(data):
    for l in data:
        for i in l:
            print i,
        print
def main():
    f = file(finput)
    T = int(f.readline())
    for i in range(1, T+1):
        N, M = map(int, f.readline().split())
        data = [map(int, f.readline().split()) for x in range(N)]
        #show( data)
        print 'Case #%d: %s'%(i, solve(data, N, M))
        #f.readline()
    pass

if __name__=='__main__':
    main()

