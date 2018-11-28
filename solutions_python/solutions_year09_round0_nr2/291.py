#!/usr/bin/env python
#-*- coding: utf-8 -*-


H = 0
W = 0

class Int(object):
    num = None
    direction = None
    label = None

    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def __repr__(self):
        return str(self.num)

    def __cmp__(self, other):
        if isinstance(other, int):
            return self.num.__cmp__(other)
        else:
            return self.num.__cmp__(other.num)


def calc(area):
    global H, W
    for i in range(H):
        for j in range(W):
            direction = []
            if i > 0:
                direction.append(area[i-1][j])
            if j > 0:
                direction.append(area[i][j-1])
            if j + 1 < W:
                direction.append(area[i][j+1])
            if i + 1 < H:
                direction.append(area[i+1][j])

            if not direction:
                area[i][j].direction = -1
            else:
                min_Int = min(direction)
                if area[i][j] <= min(direction):
                    area[i][j].direction = -1
                else:
                    area[i][j].direction = min_Int

def mark(area):
    global H, W
    char = 97
    for i in range(H):
        for j in range(W):
            target = area[i][j]
            while True:
                if target.direction == -1:
                    if target.label:
                        area[i][j].label = target.label
                    else:
                        area[i][j].label = target.label = chr(char)
                        char += 1
                    break
                else:
                    target = target.direction


T = int(raw_input())

for i in range(T):
    H, W = [int(j) for j in raw_input().split()]
    area = []
    for j in range(H):
        area.append([Int(int(k)) for k in raw_input().split()])
    calc(area)
    mark(area)
    print 'Case #%d:' % (i+1)
    for i in area:
        print ' '.join([j.label for j in i])
