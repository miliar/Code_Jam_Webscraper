from sys import stdin

def searchpath(root, pathlist):
    while pathlist and pathlist[0] in root:
        root = root[pathlist[0]]
        pathlist.pop(0)
    return root, pathlist

def addpath(d, pathlist):
    for name in pathlist:
        d[name] = {}
        d = d[name]

def solvecase(old, new):
    root = {'':{}}
    for d in old:
        dd, pathlist = searchpath(root, d.split('/'))
        if pathlist:
            addpath(dd, pathlist)
    total = 0
    for d in new:
        dd, pathlist = searchpath(root, d.split('/'))
        total += len(pathlist)
        addpath(dd, pathlist)
    return total

T = int(stdin.readline())
for i in range(T):
    N, M = map(int, stdin.readline().split())
    old = [stdin.readline().strip() for n in range(N)]
    new = [stdin.readline().strip() for m in range(M)]
    print "Case #%d: %d" % (i+1, solvecase(old, new))
