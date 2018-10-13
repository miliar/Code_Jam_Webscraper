from random import random
from math import sqrt
def ints():
    return map(int, raw_input().split())

num_cases, = ints()

def dist(v, w):
    dx = w[0] - v[0]
    dy = w[1] - v[1]
    return sqrt(dx*dx + dy*dy)

def is_valid(r, positions):
    N = len(r)
    for i, v in enumerate(positions):
        for j in xrange(i+1, N):
            w = positions[j]
            if dist(v, w) + 0.0001 < r[i] + r[j]:
                return False
    return True

def get_choice(N, W, L):
    positions = []
    for i in xrange(N):
        x = random() * W
        y = random() * L
        positions.append((x, y))
    return positions

for case_num in xrange(1, num_cases + 1):
    N, W, L = ints()
    r = ints()
    positions = get_choice(N, W, L)
    while not is_valid(r, positions):
        positions = get_choice(N, W, L)
    print "Case #%d: %s" % (case_num, ' '.join("%f %f" % pos for pos in positions))
