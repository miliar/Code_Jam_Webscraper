#! /usr/bin/env python

def read_grass(height, width):
    return [map(int, raw_input().replace(' ', '')) for i in range(height)]

def can_cut(height, width, grass):
    if height == 1 or width == 1:
        return True
    for x, y in [(x, y) for x in range(height) for y in range(width)]:
        if not okay(x, y, height, width, grass):
            return False
    return True

def check(apos, bpos, grass):
    ax, ay = apos
    bx, by = bpos
    return grass[ax][ay] <= grass[bx][by]

def row(grass, i):
    return grass[i]

def col(grass, i):
    return [row[i] for row in grass]

def okay(x, y, height, width, grass):
    center  = grass[x][y]
    if center == 1:
        return row(grass, x).count(1) == width or \
               col(grass, y).count(1) == height
    return True

def main():
    n = int(raw_input())

    for i in range(n):
        height, width = map(int, raw_input().split(' '))
        grass = read_grass(height, width)
        if can_cut(height, width, grass):
            print 'Case #%d: YES' % (i+1)
        else:
            print 'Case #%d: NO' % (i+1)


if __name__ == '__main__':
    main()
