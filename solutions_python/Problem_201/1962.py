#!/usr/bin/env python3
import sys
from queue import Queue
from heapq import nlargest

DATA = '''5
4 2
5 2
6 2
1000 1000
1000 1'''

class Node(object):

    def __init__(self, n):
        if n < 2:
            self.data = (0, 0)
        if n % 2:
            self.data = (n//2, n//2)
        else:
            self.data = (n//2 - 1, n//2)
        self.max = max(self.data)
        self.min = min(self.data)
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.max == other.max:
            return self.min < other.min
        else:
            return self.max < other.max

    def __repr__(self):
        return str(self.__dict__)

    def get_left(self):
        if self.data[0] == 0:
            return None
        if self.left is None:
            self.left = Node(self.data[0])
        return self.left

    def get_right(self):
        if self.data[1] == 0:
            return None
        if self.right is None:
            self.right = Node(self.data[1])
        return self.right

def stall(line):
    # inefficient
    n, k = [int(_) for _ in line.strip().split()]
    q = Queue()
    q.put(Node(n))
    nodes = []
    while not q.empty():
        root = q.get()
        if root is None:
            continue
        nodes.append(root)
        q.put(root.get_left())
        q.put(root.get_right())
    d = nlargest(k, nodes)[-1].data
    return sorted(d, reverse=True)

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        from io import StringIO
        fh = StringIO(DATA)
        oh = sys.stdout
    else:
        fh = open(sys.argv[1], 'r')
        oh = open('output.txt', 'w')
    with fh:
        with oh:
            for i, line in enumerate(fh.readlines()):
                if i == 0:
                    continue
                print('Case #{0}: {1[0]} {1[1]}'.format(i, stall(line)), file=oh)

