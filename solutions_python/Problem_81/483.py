#!/usr/bin/python

import sys
import math


def rpi(arr):
    n = len(arr)
    A = {}
    for i in range(n):
        A[i] = {'win': 0, 'all': 0, 'wp': 0, 'owp': 0, 'oowp': 0}
    for i in range(n):
        for j in range(n):
            if A[i].has_key(j):
                continue
            if arr[i][j] == '1':
                A[i][j] = 1
                A[j][i] = 0
                A[i]['win'] = A[i]['win'] + 1
                A[i]['all'] = A[i]['all'] + 1
                A[j]['all'] = A[j]['all'] + 1
            elif arr[i][j] == '0':
                A[i][j] = 0
                A[j][i] = 1
                A[j]['win'] = A[j]['win'] + 1
                A[i]['all'] = A[i]['all'] + 1
                A[j]['all'] = A[j]['all'] + 1
        A[i]['wp'] = float(A[i]['win']) / A[i]['all']
  #      print A[i]
    for i in range(n):
        twp = 0
        t = 0
        for j in range(n):
            if i == j or not A[i].has_key(j):
                continue
 #           print "j: %d win %d, all: %d" % (j, A[j]['win'], A[j]['all'])
            twp = twp + float(A[j]['win'] - A[j][i]) / (A[j]['all'] - 1)
            t = t + 1
 #           print twp, t
        A[i]['owp'] = twp / t;
 #       print i, " owp", A[i]['owp']
    for i in range(n):
        towp = 0
        t = 0
        for j in range(n):
            if i == j or not A[i].has_key(j):
                continue
            towp = towp + A[j]['owp']
            t = t + 1
        A[i]['oowp'] = towp / t
    output = []
    for i in range(n):
        rpi = A[i]['wp'] * 0.25 + A[i]['owp'] * 0.50 + A[i]['oowp'] * 0.25
        output.append(rpi)
#        print A[i]['win'], A[i]['wp'], A[i]['owp'], A[i]['oowp']
    return output

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if not len(argv) == 2:
        print >>sys.stderr, "Usage: store-credit.py infile"

    infile = argv[1]
    f = open(infile, 'r')
    N = int(f.readline())

    for i in range(N):
        T = int(f.readline().strip())
        arr = []
        for j in range(T):
            arr.append(f.readline().strip())
#        arr = map(lambda x: int(x), f.readline().strip().split())
#        n, pd, pg = arr
        result = rpi(arr)
        print "Case #%d:" % (i+1) # % (i + 1, result)
        for x in result:
            print "%12f" % x
        
if __name__ == "__main__":
    sys.exit(main())

