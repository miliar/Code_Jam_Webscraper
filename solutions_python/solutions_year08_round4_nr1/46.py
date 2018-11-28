#!/usr/bin/python
''' Cheating a Boolean Tree
Google Code Jam 2008
Round 2 - Problem A
Grant Glouser <gglouser@gmail.com>
'''

import sys

DEBUG = False
def debug(*msg):
    if DEBUG:
        print ' '.join([str(x) for x in msg])

def read_int_line(f):
    return int(f.readline().rstrip())

def read_int_pair(f):
    return map(int, f.readline().rstrip().split())

def print_result(case_num, result):
    print 'Case #%d: %s' % (case_num, result)

def maybe_min(x,y):
    if x != -1 and y != -1:
        return min(x,y)
    elif x != -1:
        return x
    elif y != -1:
        return y
    else:
        return -1

def maybe_add(x,y):
    if x != -1 and y != -1:
        return x+y
    else:
        return -1

def combine_and((lz, lo), (rz, ro)):
    z = maybe_min(lz,rz)
    o = maybe_add(lo,ro)
    return (z,o)

def combine_or((lz, lo), (rz, ro)):
    z = maybe_add(lz,rz)
    o = maybe_min(lo,ro)
    return (z,o)

def eval_tree(tree, pos):
    if tree[pos][0] == 'VAL':
        if tree[pos][1] == 0:
            return (0,-1)
        else:
            return (-1,0)
    else:
        left = eval_tree(tree, 2*pos+1)
        right = eval_tree(tree, 2*pos+2)
        if tree[pos][0] == 'AND':
            # AND
            (z,o) = combine_and(left,right)
            if tree[pos][1] == 1:
                (z2,o2) = combine_or(left,right)
                z2 = maybe_add(z2, 1)
                o2 = maybe_add(o2, 1)
                z = maybe_min(z,z2)
                o = maybe_min(o,o2)
            debug('pos', pos, '=>', (z,o))
            return (z,o)
        else:
            # OR
            (z,o) = combine_or(left,right)
            if tree[pos][1] == 1:
                (z2,o2) = combine_and(left,right)
                z2 = maybe_add(z2, 1)
                o2 = maybe_add(o2, 1)
                z = maybe_min(z,z2)
                o = maybe_min(o,o2)
            debug('pos', pos, '=>', (z,o))
            return (z,o)

def do_test_case(f, case_num):
    (M,V) = read_int_pair(f)
    debug((M,V))
    
    tree = []
    for i in range((M-1)/2):
        (G,C) = read_int_pair(f)
        if G == 1:
            op = 'AND'
        else:
            op = 'OR'
        tree.append((op,C))
    for i in range((M+1)/2):
        I = read_int_line(f)
        tree.append(('VAL', I))
    debug(tree)
    
    e = eval_tree(tree, 0)
    debug('eval =>', e)
    
    result = e[V]
    if result == -1:
        result = 'IMPOSSIBLE'
    print_result(case_num, result)

def main(f):
    n = read_int_line(f)
    for i in range(n):
        do_test_case(f, i+1)

if __name__ == '__main__':
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == '-d':
            DEBUG = True
    main(sys.stdin)
