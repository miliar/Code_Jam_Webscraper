#!/usr/bin/env python
#-*- coding:utf-8 -*-
 
import sys
rdl = sys.stdin.readline

class Node(object):
    def __init__(self, name):
        self.name = name
        self.children = dict()
    def append(self, dir_name):
        #print dir_name[0]
        if dir_name[0] in self.children:
            if len(dir_name) > 1:
                return self.children[dir_name[0]].append(dir_name[1:])
            else:
                return 0
        new_node = Node(dir_name[0])
        self.children[dir_name[0]] = new_node
        if len(dir_name) > 1:
            return 1 + new_node.append(dir_name[1:])
        return 1
        

def process(case):
    """precessing case #"""
    root = Node('')
    
    N, M = [int(i) for i in rdl().split()]
    
    for i in xrange(N):
        dir_name = rdl().replace("\n", '').split('/')[1:]
        root.append(dir_name)
    
    total = 0
    for i in xrange(M):
        dir_name = rdl().replace("\n", '').split('/')[1:]
        total += root.append(dir_name)
    
    
    return total
 
cases = int(rdl())
for case in xrange(1, cases+1):
    print "Case #%d:"%case, process(case)