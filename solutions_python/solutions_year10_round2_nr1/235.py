
def addDirs(splitDirs, dirDict):
    if len(splitDirs) == 0:
        return 0
    rootDir = splitDirs[0]
    mkDir = 0
    if rootDir not in dirDict.keys():
        dirDict[rootDir] = {}
        mkDir = 1
    return addDirs(splitDirs[1:], dirDict[rootDir]) + mkDir
             
def solve(f):
    N, M = map(int, f.readline().split())
    directories = {}
    for _ in xrange(N):
        addDirs(f.readline().strip().split('/')[1:], directories)
    mkDirs = 0
    for _ in xrange(M):
        mkDirs += addDirs(f.readline().strip().split('/')[1:], directories)
    return mkDirs
    

with open('A-large.in', 'r') as f:
    T = int(f.readline())
    results = [solve(f) for i in xrange(T) ]
    for i in xrange(T):
        print "Case #%d: %s" % (i+1, results[i])