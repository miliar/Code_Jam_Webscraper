from sys import stdin
from math import floor, ceil


class Tree(object):
    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.max_min = int(floor((max - min - 1) / 2.0))
        self.max_max = int(ceil((max - min - 1) / 2.0))
        self.parent = None
        self.left = None
        self.right = None

    def find_leaf(self):
        if self.left is not None and self.left.max_min == self.max_min and self.left.max_max == self.max_max:
            return self.left.find_leaf()
        elif self.right is not None:
            return self.right.find_leaf()
        else:
            return self

    def split(self):
        mid = int(floor((self.min + self.max - 1) / 2))
        self.left = Tree(self.min, mid)
        self.right = Tree(mid + 1, self.max)
        self.left.parent = self
        self.right.parent = self
        self.propogate_up()

    def propogate_up(self):
        if self.left.max_min >= self.right.max_min and self.left.max_max >= self.right.max_max:
            self.max_min = self.left.max_min
            self.max_max = self.left.max_max
        else:
            self.max_min = self.right.max_min
            self.max_max = self.right.max_max
        if self.parent is not None:
            self.parent.propogate_up()

T = int(stdin.readline())
for case in range(1, T + 1):
    (N, K) = map(int, stdin.readline().split())

    root = Tree(0, N)
    max_min = root.max_min
    max_max = root.max_max

    for k in range(0, K):
        leaf = root.find_leaf()
        max_min = leaf.max_min
        max_max = leaf.max_max
        leaf.split()

    print("Case #%d: %d %d" % (case, max_max, max_min))

