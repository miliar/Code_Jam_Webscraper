#!/usr/bin/env python

import sys
import re

file = open(sys.argv[1])

def next_line():
    return file.readline()[:-1]

class Tree:
    pass

def parse_tree(num_lines):
    entire_tree = ''
    for i in range(num_lines):
        entire_tree = entire_tree + next_line()
    
    remake = ''
    for s in entire_tree.split():
        if s != '(':
            remake = remake + s + ','
        else:
            remake = remake + s
    remake = remake[:-1] #last trailing comma
    remake2 = ''
    alpha = False
    for char in remake:
        if char.isalpha() and not alpha:
            remake2 = remake2 + "'"
            alpha = True
        elif alpha and not char.isalpha():
            remake2 = remake2 + "'"
            alpha = False
        remake2 = remake2 + char
    return eval(remake2)

def traverse_tree(tree, words):
    try:
        len(tree)
    except Exception:
        return tree
    probability = tree[0]
    if len(tree) == 4:
        descriptor = tree[1]
        if descriptor in words:
            return probability * traverse_tree(tree[2],words)
        else:
            return probability * traverse_tree(tree[3],words)
    elif len(tree) == 1:
        return probability

N = int(next_line())
for i in range(1, N+1):
    L = int(next_line())
    tree = parse_tree(L)
    A = int(next_line())

    print "Case #%d:"  % i
    for i in range(A):
        descriptors = []
        words = next_line().split()
        words = words[2:]
        p = 1 * traverse_tree(tree, words)
        print "%.7f" % p

