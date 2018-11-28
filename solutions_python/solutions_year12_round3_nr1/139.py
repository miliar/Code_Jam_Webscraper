#!/usr/bin/python

import re
import sys
#from string import maketrans

input_file = open('A-large.in')
output_file = open('A-large.out', 'w')

T = int(input_file.readline())


class Node:
    def __init__(self, parents):
        self.visited = False
        self.parents = parents

def reset(nodes):
    for node in nodes:
        node.visited = False

def find_d(node, nodes):
    to_visit = [node]
    while True:
        if len(to_visit) == 0:
            return "No"
        cur = nodes[to_visit.pop(0)]
        if cur.visited == True:
            return "Yes"
        cur.visited = True
        to_visit.extend(cur.parents)

for t in range(T):

    N = int(input_file.readline())
    nodes = []
    for i in range(N):
        line = map(int, input_file.readline().split(' '))
        nodes.append(Node([e-1 for e in line[1:]]))
        
    for i in range(N):
        reset(nodes)
        result = find_d(i, nodes)
        if result == "Yes":
            break
    
    
    output_file.write("Case #" + str(t + 1) + ": " + result + "\n")

input_file.close()
output_file.close()
