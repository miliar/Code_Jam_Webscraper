#!/usr/bin/python

import sys


def read_string():
    return sys.stdin.readline().strip()

def read_int():
    return int( read_string() )

def read_int_list():
    return [ int( x ) for x in read_string().split() ]

def all_perms( k_list ):
    if len( k_list ) <= 1:
        yield k_list
    else:
        for perm in all_perms( k_list[1:] ):
            for i in range(len(perm)+1):
                yield perm[:i] + k_list[0:1] + perm[i:]


N = read_int()

for n in range( N ):

    k = read_int()
    S = read_string()
    best = len( S ) + 1

    for p in all_perms( [ x for x in range( k ) ] ):
        #ps = ''
        last = None
        count = 0
        for block in range( len(S)/k ):
            offset = block*k
            for c in p:
                letter = S[ offset + c ]
                #ps += letter
                #print ( last, letter, letter != last )
                if letter != last:
                    last = letter
                    count += 1
        #print count, ps
        if count < best:
            best = count

    print 'Case #%i:' % ( n + 1 ), best
