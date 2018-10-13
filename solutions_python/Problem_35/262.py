#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import string

EMPTY = '0'

def mymin(iterable):
    mini = 0
    min = iterable[mini]
    for i, j in enumerate(iterable[1:]):
        if j < min:
            min = j
            mini = i
    return mini

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [EMPTY] * (width * height)

    def fetch(self, i, j):
        return self.data[j + self.width * i]

    def set(self, i, j, value):
        self.data[j + self.width * i] = value

    def set_row(self, row, iterable):
        for j, v in enumerate(iterable):
            self.set(row, j, v)

    def neighbors(self, i, j):
        def valid(d):
            if d[0] >= 0 and d[0] < self.height \
                    and d[1] >= 0 and d[1] < self.width:
                        return True
        n = [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]
        return filter(valid, n)

    def next(self, i, j):
        c = int(self.fetch(i, j))
        n = self.neighbors(i, j)
        v = [int(self.fetch(*k)) for k in n]
        try:
            p = min(v)
        except:
            return None

        if c <= p:
            return None

        return n[v.index(p)]

    def is_sink(self, i, j):
        if self.next(i, j) is None:
            return True
        return False

    def sinks(self):
        s = []
        for i in range(self.height):
            for j in range(self.width):
                if self.is_sink(i, j):
                    s.append((i, j))
        return s

    def replace(self, old, new):
        for i, elem in enumerate(self.data):
            if elem == old:
                self.data[i] = new

    def dimensions(self):
        return self.width, self.height

    def beautify(self):
        index = 0
        for elem in self.data:
            if str(elem) not in string.ascii_lowercase:
                self.replace(elem, string.ascii_lowercase[index])
                index += 1

    def __repr__(self):
        s = ''
        for i in range(self.height):
            for j in range(self.width):
                s += '%s ' % str(self.fetch(i, j))
            if i != self.height - 1:
                s += '\n'
        return s

def solve(input, W, H):
    last = 0
    B = Map(W, H)
    sinks = input.sinks()
    for i,sink in enumerate(sinks):
        B.set(*(sink + (i+1,)))
    for i in range(H):
        for j in range(W):
            stack = []
            current = (i, j)
            while B.fetch(*current) is EMPTY:
                # not a sink
                stack.append(current)
                current = input.next(*current)
            # found a sink
            number = B.fetch(*current)
            for elem in stack:
                B.set(*(elem + (number,)))
    return B

if __name__ == '__main__':
    N = int(raw_input())
    for i in range(N):
        H, W = [int(k) for k in raw_input().strip().split()]
        A = Map(W, H)
        for j in range(H):
            A.set_row(j, [int(j) for j in raw_input().strip().split()])
        ans = solve(A, W, H)
        ans.beautify()
        print "Case #%d:" % (i + 1)
        print ans
        

