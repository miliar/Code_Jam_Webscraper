#!/usr/bin/python

DATASET = 'large'
IFILE = DATASET + '.in'
OFILE = DATASET + '.out'

def solve(N, K):
    m = 2**N
    return (K % m) == m-1

ifile = open(IFILE, 'r')
ofile = open(OFILE, 'w')
T = int(ifile.readline())
for i in xrange(T):
    line = ifile.readline().split(' ')
    N = int(line[0])
    K = int(line[1])
    ofile.write('Case #%s: %s\n' % (i+1, 'ON' if solve(N, K) else 'OFF'))
ifile.close()
ofile.close()
