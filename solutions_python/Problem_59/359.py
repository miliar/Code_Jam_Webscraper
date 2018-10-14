#!/usr/bin/python

from sys import *
from functools import *
import operator

def read_int_list(f):
    l = f.readline().split('\n')[0].split(' ')
    l = map(int, l)
    return list(l)

def find(f, l):
    for x in l:
        if f(x):
            return x
    return None

class Tree:
    def __init__(self, ):
        self.root = TreeNode(None)
    def add_if_needed(self, path):
        
        n_added = 0
        path_l = path.split('/')[1:]

        cur_node = self.root
        for d in path_l:
            #print('#',d)
            # trovo chi mi interessa
            childs = cur_node.childs
            next_node = find(lambda c: c.label == d, childs)
            if next_node == None:
                #we have to add
                n_added += 1
                new_node = TreeNode(d)
                cur_node.addChild(new_node)
                cur_node = new_node
            else:
                # we found it
                cur_node = next_node
            

        # if actually added
        return n_added
        
    

class TreeNode:
    def __init__(self, label):
        self.childs = []
        self.label = label
    def addChild(self, node):
        self.childs.append(node)

# main

f = open(argv[1])
T = read_int_list(f)[0]

for t in range(T):
    n_m = read_int_list(f)
    N = n_m[0]
    M = n_m[1]

    tree = Tree()
    
    built_paths = [f.readline().split('\n')[0] for i in range(N)]
    added = [tree.add_if_needed(p) for p in built_paths]
    
    new_paths = [f.readline().split('\n')[0] for i in range(M)]
    added = [tree.add_if_needed(p) for p in new_paths]
    n_added = reduce(operator.add, added)
    res_str = 'Case #%d: %d' % (t+1, n_added)
    print(res_str)
    
    



