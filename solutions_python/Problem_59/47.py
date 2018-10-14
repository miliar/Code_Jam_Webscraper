#!/usr/bin/env python

import sys
input = sys.stdin

def add_dir(dirs, string):
    p = string.find("/")
    cnt = 0
    while p != -1:
        if string[:p] not in dirs:
            dirs.add(string[:p])
            cnt += 1
        p = string.find("/", p + 1)
    if string not in dirs:
        dirs.add(string)
        cnt += 1
    return cnt

def main():
    T = int(input.readline())
    for t in range(1, T + 1):
        N, M = map(int, input.readline().split())
        dirs = set([""])
        for i in range(N):
            add_dir(dirs, input.readline().strip())
        CNT = 0
        for i in range(M):
            CNT += add_dir(dirs, input.readline().strip())
        print "Case #%d: %s" % (t, CNT)
    return 0

if __name__ == "__main__":
    main()

