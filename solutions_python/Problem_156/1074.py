import sys
import math
from heapq import *

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return map(int, sys.stdin.readline().strip().split(' '))

def comer(a):
    a = [x - 1 for x in a if x > 1]
    return sorted(a)

def dividir(a):
    last = a[-1]
    half = last / 2.0
    novos = [int(math.floor(half)), int(math.ceil(half))]
    return sorted(a[:-1] + novos)

def dividir3(a):
    last = a[-1]
    third = last / 3.0
    f = math.floor(third)
    c = math.ceil(third)
    novos = [f, f, c]
    return sorted(a[:-1] + novos)

def tempo(a):
    h = []
    heappush(h, (0, sorted(a)))
    while True:
        t, a = heappop(h)
        if sum(a) == 0:
            return t
        heappush(h, (t + 1, comer(a)))
        if a[-1] >= 4:
            heappush(h, (t + 1, dividir(a)))
            heappush(h, (t + 2, dividir3(a)))

T = read_int()
for n in xrange(1, T + 1):
    D = read_int()
    P = read_ints()
    print 'Case #%d: %s' % (n, tempo(P))

