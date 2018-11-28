#!/usr/bin/python

class directory:
    def __init__(self, name):
        self.name = name
        self.lookup = {}
        self.nodes = []

    def __contains__(self, dir):
        if dir in self.lookup.keys():
            return True

    def add(self, node):
        self.lookup[node.name] = len(self.nodes)
        self.nodes.append(node)

    def get(self, dir):
        if dir in self:
            return self.nodes[ self.lookup[dir] ]

def add_path(root, path):
    if path == '/':
        return 0
    path = path.split('/')
    path.pop(0)
    curdir = root
    count = 0
    for dir in path:
        if dir not in curdir:
            # Create the rest of the paths
            curdir.add( directory(dir) )
            count += 1
        curdir = curdir.get(dir)
    return count

cases = int(raw_input())
for case in range(1,cases+1):
    M, N = map(int, raw_input().split())
    root = directory('/')
    count = 0
    for d in range(M):
        add_path(root, raw_input())
    for d in range(N):
        count += add_path(root, raw_input())
    print 'Case #%d: %d' % (case, count)
