#!/usr/bin/env python


def parse_paths(f):
    num_exist, num_create = [int(x) for x in f.readline().strip().split()]
    exist = set()
    to_create = []

    for x in range(num_exist):
        tup = tuple(f.readline().strip().split('/')[1:])
        exist.add(tup)

    for x in range(num_create):
        L = f.readline().strip().split('/')[1:]
        to_create.append(L)

    return exist, to_create



class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = {}

    def check(self, v):
        return v in self.children

    def add_child(self, v):
        if self.check(v):
            return False
        else:
            self.children[v] = Node(v)
            return True

    def add_children(self, childs):
        if not childs:
            return 0
        else:
            h = childs[0]
            t = childs[1:]
            curr = self.add_child(h)
            child = self.children[h]
            return curr + child.add_children(t)

    def populate(self, s):
        for dir in s:
            self.add_children(dir)


if __name__ == '__main__':
    import sys

    f = open(sys.argv[1], 'r')

    tests = int(f.readline().strip())

    for i in range(tests):
        exist, to_create = parse_paths(f)
        #print "exist", exist

        tree = Node('')
        mk = 0
        tree.populate(exist)

        for dir in to_create:
            added = tree.add_children(dir)
            mk += added

        print "Case #%s: %s" % (i+1, mk)
