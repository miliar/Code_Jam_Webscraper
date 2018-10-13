import sys
import numpy as np

class Region:
    def __init__(self, initial, i, j):
        self.initial = initial
        self.left = j
        self.right = j
        self.top = i
        self.bottom = i

    def __repr__(self):
        return "Region(initial: %s, top: %d, right: %d, bottom: %d, left %d)" % (self.initial, self.top, self.right, self.bottom, self.left)


def conflict(r1, r2):
    if r1.right >= r2.left and r1.left <= r2.right:
        if r1.top <= r2.bottom and r1.bottom >= r2.top:
            return True
        if r1.bottom >= r2.top and r1.top <= r2.bottom:
            return True
    if r1.left <= r2.right and r1.right >= r2.left:
        if r1.top <= r2.bottom and r1.bottom >= r2.top:
            return True
        if r1.bottom >= r2.top and r1.top <= r2.bottom:
            return True
    return False


num_cases = int(sys.stdin.readline().strip())
matrix = None
untouchable = set()
initials = {}

def check_conf(r1):
    if r1.top < 0 or r1.right >= len(matrix[0]) or r1.bottom >= len(matrix) or r1.left < 0:
        return True
    for r2 in initials:
        if r1 is r2:
            continue
        if conflict(r1, r2):
            # print r1
            # print r2
            # print
            return True
    return False

def row_up(r1):
    r1.top -= 1
    if check_conf(r1):
        r1.top += 1
        return False
    return True

def row_right(r1):
    r1.right += 1
    if check_conf(r1):
        r1.right -= 1
        return False
    return True

def row_down(r1):
    r1.bottom += 1
    if check_conf(r1):
        r1.bottom -= 1
        return False
    return True

def row_left(r1):
    r1.left -= 1
    if check_conf(r1):
        r1.left += 1
        return False
    return True

def expand(r1):
    while True:
        if not row_up(r1):
            break
    while True:
        if not row_right(r1):
            break
    while True:
        if not row_down(r1):
            break
    while True:
        if not row_left(r1):
            break

def fill_region(r1):
    for i in xrange(r1.top, r1.bottom + 1):
        for j in xrange(r1.left, r1.right + 1):
            try:
                matrix[i][j] = r1.initial
            except:
                print i, j, r1.initial
                sys.exit()

def fill():
    # while remaining > 0:
    for r1 in initials:
        expand(r1)
        fill_region(r1)
        

for case in xrange(num_cases):
    rows, cols = map(int, sys.stdin.readline().strip().split())
    matrix = []
    initials = []
    for r in xrange(rows):
        matrix.append(list(sys.stdin.readline().strip()))
    for i in xrange(rows):
        for j in xrange(cols):
            if matrix[i][j] != "?":
                initials.append(Region(matrix[i][j], i, j))
    fill()
    print "Case #%d:" % (case + 1)
    for row in matrix:
        print "".join(row)
