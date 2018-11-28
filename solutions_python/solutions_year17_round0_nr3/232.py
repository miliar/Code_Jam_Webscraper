__author__ = 'sware'

import sys, collections, heapq

handle = file(sys.argv[1])
handleout = file(sys.argv[2], 'w')

for case in xrange(int(handle.readline())):
    N, K = map(int, handle.readline().split())
    ofdiff = collections.defaultdict(lambda : 0)
    ofdiff[N] = 1
    heap = [-N]
    while K > 0:
        diff = - heapq.heappop(heap)
        numwithdiff = ofdiff[diff]
        diffr = diff / 2
        if diff % 2:
            diffl = diffr
        else:
            diffl = diffr-1
        if diffr not in ofdiff:
            heapq.heappush(heap, -diffr)
        ofdiff[diffr] += numwithdiff
        if diffl not in ofdiff:
            heapq.heappush(heap, -diffl)
        ofdiff[diffl] += numwithdiff
        K -= numwithdiff
    handleout.write('Case #{}: {} {}\n'.format(case+1, diffr, diffl))