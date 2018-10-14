import sys

class Node:
    def __init__(self, size):
        self.size = size
        self.right = None
        self.left = None
        self.cached = None

    def split(self):
        self.cached = None
        if self.left and self.right:
            if self.right.best() > self.left.best():
                return self.right.split()
            else:
                return self.left.split()
        else:
            if self.size % 2 == 1:
                self.left = Node(self.size // 2)
                self.right = Node(self.size // 2)
                return (self.size // 2, self.size // 2)
            else:
                self.left = Node(self.size // 2 - 1)
                self.right = Node(self.size // 2)
                return (self.size // 2 - 1, self.size // 2)

    def best(self):
        if self.cached:
            return self.cached
        if self.left and self.right:
            self.cached = max(self.left.best(), self.right.best())
            return self.cached
        else:
            if self.size % 2 == 1:
                self.cached = (self.size // 2, self.size // 2)
                return self.cached
            else:
                self.cached = (self.size // 2 - 1, self.size // 2)
                return self.cached


T = int(sys.stdin.readline().strip())
for t in range(1, T+1):
    N, K = sys.stdin.readline().strip().split()
    N = int(N)
    K = int(K)
    last = None
    root = Node(N)
    for i in range(K):
        last = root.split()
    print("Case #%s: %s %s" % (t, last[1], last[0]))
