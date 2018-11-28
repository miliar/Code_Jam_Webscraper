#!/usr/bin/python

import sys

def emit(text, *args):
    msg = text % args
    sys.stderr.write(msg)
    sys.stdout.write(msg)

def getline():
    return sys.stdin.readline().rstrip('\n')

v_1 = 1
v_i = 2
v_j = 3
v_k = 4

i_trans = [ v_i, -v_1, v_k, -v_j ]
j_trans = [ v_j, -v_k, -v_1, v_i ]
k_trans = [ v_k, v_j, -v_i, -v_1 ]

conv = { 'i': v_i, 'j': v_j, 'k': v_k }

def quat(old, new):
    if old == v_1:
        return new
    if old < 0:
        return - (quat(- old, new))
    if new < 0:
        return - (quat(old, - new))
    if old == v_i:
        return i_trans[new - v_1]
    if old == v_j:
        return j_trans[new - v_1]
    if old == v_k:
        return k_trans[new - v_1]

def i_end(s):
    i_val = v_1
    for i in range(len(s) - 2):
        i_val = quat(i_val, s[i])
        if i_val == v_i:
            return i;
    return None

def k_start(s, iend):
    k_val = v_1
    for k in range(len(s) - 1, iend + 1, -1):
        k_val = quat(s[k], k_val)
        if k_val == v_k:
            return k;
    return None
    
def solve(l, x, s):
    if l * x < 3:
        return "NO"
    # brute force solution
    s = [ conv[c] for c in s ]
    s = s * x
    iend = i_end(s)
    if iend is None:
        return "NO"
    kstart = k_start(s, iend)
    if kstart is None:
        return "NO"
    sys.stderr.write("len = %d, iend = %d, kstart = %d\n" % (len(s), iend, kstart))
    j_val = v_1
    for j in range(iend + 1, kstart):
        j_val = quat(j_val, s[j])
    if j_val == v_j:
        return "YES"
    return "NO"

ncases = int(getline())

for casenr in range(1, ncases+1):
    l, x = [ int(s) for s in getline().split() ]
    s = getline().strip()
    emit("Case #%d: %s\n", casenr, solve(l, x, s))
