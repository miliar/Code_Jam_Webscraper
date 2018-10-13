#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="nsho"
__date__ ="$2010/05/23 0:58:20$"

import sys

class TNode(object):
    def __init__(self, name, parent):
        self.name = name
        self.child = dict()
        self.parent = parent

    def add(self, child_name):
        child = TNode(child_name, self)
        self.child[child_name] =  child
        return child
    def contains(self, child_name):
        return self.child.get(child_name)


def node_search(root_node, path):
    cur = root_node
    n = 0
    path = path.rstrip().rstrip('/')
    for pname in path.split('/')[1:]:
        child_node = cur.contains(pname)
        if child_node is None:
            child_node = cur.add(pname)
            n += 1
        cur = child_node
    return n

fname = sys.argv[1]
outf = fname + ".out"
with open(fname, 'r') as fp:
    line = fp.readline()
    nr_case = int(line)
    case = 1
    with open(outf, 'w') as out_fp:
        for _i in range(0, nr_case):
            root_node = TNode('/', None)
            nr_exist, nr_req = fp.readline().split()
            nr_exist = int(nr_exist)
            nr_req = int(nr_req)
            n = 0
            for _j in xrange(0, nr_exist):
                node_search(root_node, fp.readline())
            for _j in xrange(0, nr_req):
                n += node_search(root_node, fp.readline())
            outline = "Case #%d: %d\n" % (case, n)
            out_fp.write(outline)
            print outline,
            case += 1



