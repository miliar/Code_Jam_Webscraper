#!/usr/bin/python

from sol import *

cases = next_int()

INF = 1000000

is_and = []
is_leaf = []
changable = []
node_val = []

def min_req_int(idx, is_and, val):
    tt = [ min_req(idx*2,True), min_req(idx*2+1,True) ]
    ff = [ min_req(idx*2,False), min_req(idx*2+1,False) ]

    if is_and:
        if val:
            return tt[0] + tt[1]
        else:
            return min( ff[0], ff[1] )
    else:
        if val:
            return min( tt[0], tt[1] )
        else:
            return ff[0] + ff[1]

cached = {}

def min_req(idx,val):
    hash = idx*2 + val
    if hash in cached:
        return cached[hash]

    if is_leaf[idx]:
        if node_val[idx] == val:
            return 0
        else:
            return INF

    best = min_req_int(idx, is_and[idx], val)
    if changeable[idx]:
        act = 1+min_req_int(idx, is_and[idx]==False, val)
        if act < best:
            best = act

    cached[hash] = best
    return best

for case_num in range(1,cases+1):
    cached = {}

    nodes = next_int()
    desired = next_int()==1

    is_and = mytab(nodes+1,False)
    is_leaf = mytab(nodes+1,False)
    changeable = mytab(nodes+1,False)
    node_val = mytab(nodes+1,False)

    idx = 1
    for i in range(0,(nodes-1)/2):
        is_and[idx] = next_int()==1
        changeable[idx] = next_int()==1
        is_leaf[idx] = False
        idx += 1

    for i in range(0,(nodes+1)/2):
        node_val[idx] = next_int()==1
        is_leaf[idx] = True
        idx += 1

    res = min_req(1,desired)

    if res < INF:
        res = str(res)
    else:
        res = "IMPOSSIBLE"

    print 'Case #%d: %s' % (case_num, res)
