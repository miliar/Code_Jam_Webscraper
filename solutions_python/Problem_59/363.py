#!/usr/bin/python

import sys

def processDirs(directories):
    res = list()
    for path in directories:
        dirs = path.split('/')
        dirs = dirs[1:]
        for j in range(len(dirs)):
            tmp = '/'.join(dirs[:j + 1])
            if tmp not in res:
                res.append(tmp)
    return res

nbTestCase = int(sys.stdin.readline())
for i in range(1, nbTestCase + 1):
    (N, M) = map(lambda x:int(x), sys.stdin.readline().split())
    (directories, mkdirectories) = (list(), list())
    for j in range(N):
        directories.append(sys.stdin.readline().rstrip())
    for j in range(M):
        mkdirectories.append(sys.stdin.readline().rstrip())
    directories = processDirs(directories)
    mkdirectories = processDirs(mkdirectories)
    res = 0
    for dir in mkdirectories:
        if dir not in directories:
            res += 1
    print("Case #%d: %d" % (i, res))