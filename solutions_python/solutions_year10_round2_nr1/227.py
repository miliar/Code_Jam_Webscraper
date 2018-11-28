#-*-coding:utf-8-*-

import sys

fh = open(sys.argv[1])
T = int(fh.readline())

class Node(object):
    def __init__(self, name):
        self.name = name
        self.children = {}
        #self.nodes = Node()
        pass
    def add(self, names):
        #names = path.strip('/').split('/')
        if len(names) == 0: return 0
        num_gen = 0
        if names[0] not in self.children:
            child = Node(names[0])
            self.children[names[0]] = child
            num_gen += 1
        else:
            child = self.children[names[0]]
            pass
        num_gen += child.add(names[1:])
        return num_gen
    pass

for cn in range(1, T + 1):
    N, M = [int(x) for x in fh.readline().split(' ')]
    dirset = Node('')
    num_nodes = 0
    for i in range(N):
        dirset.add(fh.readline().strip().strip('/').split('/'))
        pass
    for j in range(M):
        num_nodes += dirset.add(fh.readline().strip().strip('/').split('/'))
        #num_nodes += dirset.add(fh.readline().strip())
        pass
    print('Case #{0}: {1}'.format(cn, num_nodes))
    pass

