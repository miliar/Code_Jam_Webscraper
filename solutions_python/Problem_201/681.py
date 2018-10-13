#! /usr/bin/python

import os
import sys
import copy

def debug(msg):
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        sys.stderr.write('%s' % msg)
        sys.stderr.write('\n')

def split(block_size):
    if block_size % 2:
        r = (block_size - 1) / 2
        return (r, r)
    else:
        return (block_size / 2, block_size / 2 - 1)

def insert_sorted(L, block):
    block_size = block[0]
    if not L:
        return [block]
    elif block_size > L[0][0]:
        return [block] + L
    elif block_size == L[0][0]:
        new_block_count = block[1] + L[0][1]
        return [(block_size, new_block_count,)] + L[1:]
    else:
        return [L[0]] + insert_sorted(L[1:], block)

def solve(N, K):
    place_blocks = [(N,1,)]
    max_placed = 0
    while True:
        debug('blocks = %s  || placed = %s' % (place_blocks, max_placed))
        #
        block_to_split = place_blocks[0]
        place_blocks = place_blocks[1:]
        block_size = block_to_split[0]
        block_count = block_to_split[1]
        new_block_size_r = split(block_size)
        place_blocks = insert_sorted(place_blocks, (new_block_size_r[0], block_count))
        place_blocks = insert_sorted(place_blocks, (new_block_size_r[1], block_count))
        max_placed += block_count
        #
        if K <= max_placed:
            return '%s %s' % (max(new_block_size_r), min(new_block_size_r))
        
    return None

sys.setrecursionlimit(15000)

T = int(sys.stdin.readline())
# For each test case
for t in range(1, T+1):
    debug(' ************* case %s' % t)
    [N, K] = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    ret = solve(N, K)
    sys.stdout.write('Case #%s: %s\n' % (t, ret))
