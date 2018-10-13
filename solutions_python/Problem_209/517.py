import sys
import math
import uuid

sys.stdin = open('A-large.in')
sys.stdout = open('A-large.out', 'w')

class Pancake:
    def __init__(self, R, H):
        self.idx = uuid.uuid4();
        self.r = float(R)
        self.h = float(H)

    def square(self):
        return math.pi * self.r * self.r

    def side(self):
        return 2.0 * math.pi * self.r * self.h

    def full(self):
        return self.side() + self.square()

    def __repr__(self):
        return "<Pancake r:%s h:%s>" % (self.r, self.h)


def flip(row, idx, size):
    for i in xrange(size):
        row[idx+i] = 1 - row[idx+i]
    return row
def solve():
    N,K = map(int, sys.stdin.readline().strip().split(' '))
    cakes = []
    for _i in range(N):
        R,H = map(int, sys.stdin.readline().strip().split(' '))
        cakes.append(Pancake(R,H))

    R0 = max(list(map(lambda x:x.r, cakes)))

    if K==N:
        return sum(list(map(lambda x:x.side(), cakes))) + math.pi * R0 * R0
    else:
        cakes.sort(key=lambda cake:cake.side(), reverse=True)
        part = cakes[:K-1]
        sides = sum(list(map(lambda x:x.side(), part)))
        if len(part)==0:
            maxr = 0
        else:
            maxr = max(list(map(lambda x:(x.r), part)))

        mx = 0

        for cake in cakes:
            if cake not in part:
                if cake.r <= maxr:
                    cur = cake.side() + math.pi * maxr * maxr
                else:
                    cur = cake.full()
                if cur > mx:
                    mx = cur

    return sides + mx



t = int(sys.stdin.readline())
for _t in range(t):
    print("Case #%d: %.9f" % (_t+1, solve()))
