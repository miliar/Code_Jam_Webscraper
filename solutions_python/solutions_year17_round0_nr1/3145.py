#!/usr/bin/env python3

for case_num in range(int(input())):
    # O(2^n) :(
    line = input().split()
    pancakes = [c == '+' for c in line[0]]
    flip_size = int(line[1])
    possible_flips = len(pancakes) + 1 - flip_size
    for i in range(2 ** possible_flips):
        bits = [(i >> j) & 1 for j in range(possible_flips)]
        new_pancakes = pancakes[:]
        for j in range(possible_flips):
            if bits[j]:
                for k in range(flip_size):
                    new_pancakes[j + k] = not new_pancakes[j + k]
        if all(new_pancakes):
            print('Case #%d: %d' % (case_num + 1, bits.count(True)))
            break
    else:
        print('Case #%d: IMPOSSIBLE' % (case_num + 1,))
