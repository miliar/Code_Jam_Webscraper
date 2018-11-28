import sys
import random

T = int(sys.stdin.readline()[:-1])

class Ken:
    def __init__(self, blocks):
        self.blocks = blocks
        self.blocks.sort()
    def choose(self, told):
        if told > self.blocks[-1]:
            return self.blocks.pop(0)
        else:
            i = 0
            while self.blocks[i] < told: i += 1
            return self.blocks.pop(i)

class Naomi:
    def __init__(self, blocks):
        self.blocks = blocks
        self.blocks.sort()
    def tell_and_choose(self):
        b = self.blocks.pop(0)
        if not self.blocks or b > self.kens_blocks[-1]:
            return b, b
        elif b > self.kens_blocks[0]:
            return random.uniform(self.kens_blocks[-1] + 0.001, 0.999), b
        else:
            return random.uniform(self.kens_blocks[-2] + 0.001, self.kens_blocks[-1] - 0.001), b

for x in range(1, T+1):
    N = int(sys.stdin.readline()[:-1])
    naomi = Naomi(map(float, sys.stdin.readline().split()))
    naomi_copy = list(naomi.blocks)
    ken = Ken(map(float, sys.stdin.readline().split()))
    ken_copy = list(ken.blocks)
    naomi.kens_blocks = ken.blocks
    y = 0
    for _ in range(N):
        t, n = naomi.tell_and_choose()
        k = ken.choose(t)
        if n > k: y += 1
#         print n, t, k
    ken = Ken(ken_copy)
    z = [n > ken.choose(n) for n in naomi_copy].count(True)
    print 'Case #{}: {} {}'.format(x, y, z)
