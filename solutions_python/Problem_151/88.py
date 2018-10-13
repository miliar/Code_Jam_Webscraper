#!/usr/bin/env python

from sys import stdin, stdout
from numpy import array, log2, floor, ceil


class Node(object):
    def __init__(self, parent, char):
        self.parent = parent
        self.char = char
        self.child = []

    def show(self, offset):
        ret = offset + self.char
        print '"%s"' % ret
        for chi in self.child: chi.show(ret)

    def cnt(self):
        ret = 1
        for chi in self.child: ret += chi.cnt()
        return ret


class Tree(object):
    def __init__(self):
        self.root = Node(None, "")

    def add(self, string):
        now = self.root
        for c in string:
            find = False
            for kodomo in now.child:
                if kodomo.char == c:
                    now = kodomo
                    find = True
                    break
                pass
            if not find:
                kodomo = Node(now, c)
                now.child.append(kodomo)
                now = kodomo
                pass
            pass

    def show(self):
        self.root.show("")

    def cnt(self):
        return self.root.cnt()

def dataset(mm, nn):
    ret = [ [a] for a in range(mm) ]
    for n in range(nn-1):
        rettmp = ret
        ret = []
        for r in rettmp:
            for m in range(mm):
                ret.append(r + [m])
                pass
            pass
        pass

    rettmp = ret
    ret = []
    for r in rettmp:
        find = True
        for m in range(mm):
            if not m in r:
                find = False
                pass
            pass
        if find: ret.append(r)
        pass
    return ret



T = int(stdin.readline())

for t in range(T):
    print "Case #%d:" % (t+1),



    theTree = Tree()

    M, N = array(stdin.readline().split()).astype(int)
    S = []
    for i in range(M): S.append(stdin.readline().strip())

    result = []

    for subset in dataset(N, M):
        theTrees = [Tree() for i in range(N)]
        for ss, sn in zip(S, subset): theTrees[sn].add(ss)
        res = 0
        for tt in theTrees: res += tt.cnt()
        result.append(res)
        pass

    ret1 = max(result)
    ret2 = 0
    for rr in result:
        if rr == ret1: ret2 += 1

    print ret1, ret2
    stdout.flush()
