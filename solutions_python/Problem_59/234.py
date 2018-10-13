#!/usr/bin/env python2.6

import sys

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return map(int, sys.stdin.readline().split())

def read_line():
    return sys.stdin.readline().strip()

def solve():
    N, M = read_ints()
    dirs = []
    for i in range(N):
        dirs.append(read_line())
    to_create = []
    for i in range(M):
        to_create.append(read_line())

    mkdir = 0;
    for create in to_create:
        paths = create.split('/')[1:]
        for i in range(1, len(paths)+1):
            path = "/" + "/".join(paths[0:i])
            if path not in dirs:
                dirs.append(path)
                mkdir += 1
    print mkdir

def main():
    T = read_int()
    
    for case in xrange(1, T + 1):
        print 'Case #%d:' % case,
        solve()

if __name__ == '__main__':
    main()
