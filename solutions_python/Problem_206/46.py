__author__ = 'sware'

import sys, collections

inputfile = file(sys.argv[1])
outputfile = file(sys.argv[2], 'w')

for case in xrange(int(inputfile.readline())):
    D, N = map(int, inputfile.readline().split())
    maxreachtime = float(0)
    for _ in xrange(N):
        K, S = map(int, inputfile.readline().split())
        K = D - K
        maxreachtime = max(maxreachtime, float(K) / float(S))
    outputfile.write('Case #{}: {}\n'.format(case+1, float(D)/ maxreachtime))
    #map(int, inputfile.readline().split())

outputfile.close()