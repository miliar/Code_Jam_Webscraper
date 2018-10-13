#! /usr/bin/python

import os, sys
from collections import OrderedDict

def debug(msg):
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        sys.stderr.write(msg)
        sys.stderr.write('\n')

T = int(sys.stdin.readline())

for t in range(1, T+1):
    [N, X] = [int(x) for x in sys.stdin.readline().split(' ')]
    file_list = [int(x) for x in sys.stdin.readline().split(' ')]
    file_list.sort()
    file_list_big = file_list[::-1]
    idx_big = 0
    idx_small = 0
    files_added = 0
    disks_used = 0
    while files_added < N:
        #if idx_big == N - idx_small:
        #    debug('imposible')
        #    break
        if file_list_big[idx_big] + file_list[idx_small] <= X:
            files_added += 2
            idx_big += 1
            idx_small += 1
        else:
            idx_big += 1
            files_added += 1
        disks_used += 1
    sys.stdout.write('Case #%s: %s\n' % (t, disks_used))
            
