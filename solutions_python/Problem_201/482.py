#! /usr/bin/env python3
import sys

def get_free_stalls_around(free_block_size, n_people):
    if n_people == 1:
        return (free_block_size // 2, (free_block_size-1) // 2)
    if n_people == free_block_size:
        return (0, 0)
    if free_block_size % 2 == 1 or (n_people-1) % 2 == 0:
        return get_free_stalls_around((free_block_size-1) // 2, n_people // 2)
    return get_free_stalls_around(free_block_size // 2, n_people // 2)

T = int(sys.stdin.readline().strip())
for t, line in enumerate(sys.stdin.readlines()):
    N, K = (int(n) for n in line.strip().split())
    print('Case #{}: {} {}'.format(t+1, *get_free_stalls_around(N, K)))
