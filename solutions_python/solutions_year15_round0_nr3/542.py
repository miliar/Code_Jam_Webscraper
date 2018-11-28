#!/usr/bin/python3

import sys

ncases = int(sys.stdin.readline().strip())

mult_table = {
     '1': {'1': '1', '-1': '-1', 'i': 'i', '-i': '-i', 'j': 'j', '-j': '-j', 'k': 'k', '-k': '-k'},
    '-1': {'1': '-1', '-1': '1', 'i': '-i', '-i': 'i', 'j': '-j', '-j': 'j', 'k': '-k', '-k': 'k'},
     'i': {'1': 'i', '-1': '-i', 'i': '-1', '-i': '1', 'j': 'k', '-j': '-k', 'k': '-j', '-k': 'j'},
    '-i': {'1': '-i', '-1': 'i', 'i': '1', '-i': '-1', 'j': '-k', '-j': 'k', 'k': 'j', '-k': '-j'},
     'j': {'1': 'j', '-1': '-j', 'i': '-k', '-i': 'k', 'j': '-1', '-j': '1', 'k': 'i', '-k': '-i'},
    '-j': {'1': '-j', '-1': 'j', 'i': 'k', '-i': '-k', 'j': '1', '-j': '-1', 'k': '-i', '-k': 'i'},
     'k': {'1': 'k', '-1': '-k', 'i': 'j', '-i': '-j', 'j': '-i', '-j': 'i', 'k': '-1', '-k': '1'},
    '-k': {'1': '-k', '-1': 'k', 'i': '-j', '-i': 'j', 'j': 'i', '-j': '-i', 'k': '1', '-k': '-1'}
}

letters = ['i', 'j', 'k']

for t in range(1, ncases+1):
    values = sys.stdin.readline().strip().split()
    l = int(values[0])
    x = int(values[1])
    substring = sys.stdin.readline().strip()

    string = substring * x
    length = len(string)

    if len(string) < 3:
        print("Case #{0}: NO".format(t))
        continue

    solution = False

    valid_i = []
    current = '1'
    for pos in range(0, length-2):
        current = mult_table[current][string[pos]]
        if current == 'i':
            valid_i.append(pos+1)

    valid_k = {}
    current = '1'
    for pos in range(length-1, 1, -1):
        current = mult_table[string[pos]][current]
        if current == 'k':
            valid_k[pos] = True

    if len(valid_i) == 0 or len(valid_k) == 0:
        print("Case #{0}: NO".format(t))
        continue

    for pi in valid_i:
        current = '1'
        for c in range(pi, length-1):
            current = mult_table[current][string[c]]
            if current == 'j' and valid_k.get(c+1, False):
                solution = True
                #print("Found valid solution for {} and {}".format(pi, c+1))
                break
        if solution:
            break

    if solution:
        print("Case #{0}: YES".format(t))
    else:
        print("Case #{0}: NO".format(t))

