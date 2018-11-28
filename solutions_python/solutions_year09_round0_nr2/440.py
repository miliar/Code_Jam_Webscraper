#!/usr/bin/env python

# North, West, East, South.

import sys
import re

moves = [(0, -1), (-1, 0), (1, 0), (0, 1)]

def show(r, h, w):
    y = 0
    while y < h:
        print str.join(" ", r[y].values())
        y = y + 1

def fillr(r, h, w):
    y = 0
    while y < h:
        x = 0
        r[y] = {}
        while x < w:
            r[y][x] = ' '
            x = x + 1
        y = y + 1

def fixr(r, h, w):
    c = 'a'
    y = 0
    while y < h:
        x = 0
        while x < w:
            if x == 0 and y == 0 and r[y][x] != c:
                rename(r, r[y][x], c, h, w)
                c = chr(ord(c) + 1)
            elif r[y][x] > c:
                if ord(r[y][x]) == ord(c) + 1:
                    c = r[y][x]
                else:
                    c = chr(ord(c) + 1)
                    rename(r, r[y][x], c, h, w)
            x = x + 1
        y = y + 1

def rename(r, old, new, h, w):
    y = 0
    while y < h:
        x = 0
        while x < w:
            if r[y][x] == old:
                r[y][x] = new
            x = x + 1
        y = y + 1

def flow(m, r, h, w, x, y, c):
    if r[y][x] != ' ':
        return
    r[y][x] = c
    sqr = (x, y, int(m[y][x]))
    for delta in moves:
        dx = x + delta[0]
        dy = y + delta[1]
        if dx < 0 or dx >= w:
            continue
        if dy < 0 or dy >= h:
            continue

        if int(m[dy][dx]) < int(sqr[2]):
            sqr = (dx, dy, int(m[dy][dx]))

    if sqr[2] < int(m[y][x]):
        dx = sqr[0]
        dy = sqr[1]
        if r[dy][dx] != ' ':
            rename(r, c, r[dy][dx], h, w)
            c = r[dy][dx]
        flow(m, r, h, w, dx, dy, c)

def resolve(m, r, h, w):
    c = 'a'
    y = 0
    fillr(r, h, w)
    while y < h:
        x = 0
        while x < w:
            flow(m, r, h, w, x, y, c)
            x = x + 1
            c = chr(ord(c)+1)
        y = y + 1

line = sys.stdin.readline()
t = int(line)


i = 0
while i < t:
    m = {}
    r = {}
    line = sys.stdin.readline()
    line = line.split(" ")
    h, w = int(line[0]), int(line[1])
    i = i + 1
    x = 0
    while x < h:
        line = sys.stdin.readline()
        m[x] = line.split()
        x = x + 1
    r = {}
    resolve(m, r, h, w)
    print "Case #%d:" % (i)
    fixr(r, h, w)
    show(r, h, w)
