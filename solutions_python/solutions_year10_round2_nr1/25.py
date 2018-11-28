#!/usr/bin/env python

from sys import stdin, stdout

class Tree(object):
    def __init__(self):
        self.subdirs = dict()
    def add_path(self, name, pos=1):
        if pos >= len(name):
            return 0
        nextpos = name.find('/', pos)
        if nextpos == -1:
            nextpos = len(name)
        subdir = name[pos:nextpos]
        if(subdir not in self.subdirs):
            self.subdirs[subdir] = Tree()
            i = 1
        else:
            i = 0
        return i + self.subdirs[subdir].add_path(name, nextpos+1)

T = int(stdin.readline())
for t in range(T):
    (N, M) = map(int, str.split(stdin.readline()))
    tr = Tree()
    for i in range(N):
        tr.add_path(stdin.readline()[:-1])
    n = 0
    for i in range(M):
        n += tr.add_path(stdin.readline()[:-1])
    stdout.write('Case #%i: %i\n' % (t+1, n))

