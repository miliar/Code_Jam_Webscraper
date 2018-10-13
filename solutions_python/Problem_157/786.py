#!/usr/bin/python3

import sys
import math
import bisect


mult_table = {
    '1': {'1': '+1', 'i': '+i', 'j': '+j', 'k': '+k'},
    'i': {'1': '+i', 'i': '-1', 'j': '+k', 'k': '-j'},
    'j': {'1': '+j', 'i': '-k', 'j': '-1', 'k': '+i'},
    'k': {'1': '+k', 'i': '+j', 'j': '-i', 'k': '-1'}
}


def mult(op1, op2):
    neg = (op1[0] == '-' or op2[0] == '-') and not (op1[0] == '-' and op2[0] == '-')
    res = mult_table[op1[1]][op2[1]]
    if neg:
        if res[0] == '-':
            res = '+' + res[1]
        else:
            res = '-' + res[1]
    return  res


def find_dijkstra(s):
    candidates = set()
    candidates.add(('', '+1'))

    for c in s:
        next_candidates = set()
        for candidate in candidates:
            parsed_str = candidate[0]
            dijkstra_value = mult(candidate[1], c)
            next_candidates.add((parsed_str, dijkstra_value))
            if parsed_str == '' and dijkstra_value == '+i':
                next_candidates.add(('i', '+1'))
            elif parsed_str == 'i' and dijkstra_value == '+j':
                next_candidates.add(('ij', '+1'))
        candidates = next_candidates
    return ('ij', '+k') in candidates


if __name__ == '__main__':
    test_count = int(sys.stdin.readline())

    for t in range(1, test_count + 1):
        #if t == 5: break
        l, x = tuple(map(int, sys.stdin.readline().split()))
        s = sys.stdin.readline().strip()
        s = list(map(lambda c: '+' + c, list(s))) * x
        found = find_dijkstra(s)
        print('Case #%d: %s' % (t, found and 'YES' or 'NO'))
