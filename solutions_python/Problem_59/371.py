#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import math

def createTree(path):
    tree = {}
    for i in path:
        tmp = tree
        for d in i.split("/")[1:]:
            if not tmp.has_key(d):
                tmp[d] = {}
            tmp = tmp[d]
    return tree

trial = int(sys.stdin.readline())
for t in range(trial):
    [n,m] = [int(j) for j in sys.stdin.readline().split()]
    exist = []
    for j in range(n): exist.append(sys.stdin.readline().rstrip())
    create = []
    for j in range(m): create.append(sys.stdin.readline().rstrip())
    #print exist
    #print create
    tree = createTree(exist)
    count = 0
    for path in create:
        tmp = tree
        for d in path.split("/")[1:]:
            if tmp.has_key(d):
                tmp = tmp[d]
                continue
            else:
                tmp[d]={}                
                tmp = tmp[d]
                count += 1
    print "Case #%d: %d"%(t+1, count)
    
