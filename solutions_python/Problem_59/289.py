#
# Google Code Jam 2010
# Roaund 1B: A. File Fix-It
# submission by EnTerr
#

import sys

f = open(sys.argv[1])
def input(): return f.readline().strip();

def mkdir(dir):
    # return number of mkdir needed, considering current state
    nn = 0
    path = dir.split('/')
    pwd = fs
    while path:
        if path[0] not in pwd:
            pwd[path[0]] = {}
            nn += 1
        pwd = pwd[path[0]]
        del path[0]
    return nn
    

for caseNo in xrange(1, int(input())+1):
    (N, M) = map(int, input().split())
    fs = {'':{}}
    cnt = 0
    for _ in range(N):
        mkdir(input())
    for _ in range(M):
        cnt += mkdir(input())
        
    print 'Case #%d: %d' % (caseNo, cnt)

