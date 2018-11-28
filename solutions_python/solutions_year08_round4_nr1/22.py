#!/usr/bin/env python

import sys

class Nope(Exception):
    pass

# node: 
# (gate_type, can_change)
# bool_val

AND=1
OR=0

INFINITE=1e12

def eval(T, i):
    if is_val(T,i):
        #print "i=", i, "T[i]=", T[i]
        return T[i]
    c1, c2 = children(T, i)
    if gate_type(T,i) == AND:
        c = (eval(T, c1) and eval(T, c2))
    else:
        c = (eval(T, c1) or eval(T, c2))
    #print "i=", i, "T[i]=", c
    return 1 if c else 0

def is_val(T, i):
    return type(T[i]) is not tuple

def gate_type(T, i):
    return T[i][0]

def children(T, i):
    return i*2+1, i*2+2

def can_change(T, i):
    if T[i][1]:
        pass
        #print "can change", i
    return T[i][1]

def count_changes_needed(T, index, V):
    if is_val(T, index):
        V1 = eval(T, index)
        if V==V1: return 0
        return INFINITE

    c1, c2 = children(T, index)

    cc1 = count_changes_needed(T, c1, V)
    #print c1, cc1
    cc2 = count_changes_needed(T, c2, V)
    #print c2, cc2

    if gate_type(T, index) == V:
        #print "MATCH"
        # both of them need to match
        r = cc1+cc2
        if can_change(T,index):
            #print "maybe changing index", index
            r = min(1+cc1, 1+cc2, r)
    else:
        r = min(cc1, cc2)

    return r

def do_trial(f):
    M, V = [int(x) for x in f.readline().split()]

    nodes = []
    for i in range((M-1)/2):
        x,y = [int(x) for x in f.readline().split()]
        nodes.append((x,y))

    for i in range((M+1)/2):
        nodes.append(int(f.readline()))

    n = count_changes_needed(nodes, 0, V)
    if n>=INFINITE: return "IMPOSSIBLE"
    return n

f = sys.stdin
#f = file("tiny.in")
count = int(f.readline())
for i in range(count):
    r = do_trial(f)
    print "Case #%d: %s" % (i+1, r)
