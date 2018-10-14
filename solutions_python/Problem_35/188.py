#!/usr/bin/env python

from __future__ import print_function, division
__metaclass__ = type

import sys, re, string
import numpy as np

class Namespace:
    pass

def apply_numeric_labels(direction, labels):
    next_value = 0
    for pos, value in np.ndenumerate(labels):
        path = []
        while value < 0:
            path.append(pos)
            d = direction[pos]
            if d == (0,0):
                value = next_value
                next_value += 1
            else:
                pos = pos[0] + d[0], pos[1] + d[1]
                value = labels[pos]
        for pos in path:
            labels[pos] = value

def numeric_to_alpha(labels):
    alphabet = string.lowercase
    inv_mapping = []
    for x in labels.flat:
        if x not in inv_mapping:
            inv_mapping.append(x)
    mapping = ''.join(alphabet[inv_mapping.index(i)]
            for i in range(len(inv_mapping)))
    return [[mapping[x] for x in row] for row in labels]

def process(test_num, data):
    print('Case #{0}:'.format(test_num))
    H, W = data.shape

    ns = Namespace()

    def try_dir(I, J):
        if 0 <= i+I <= H-1 and 0 <= j+J <= W-1:
            x = data[i+I,j+J]
            if x < ns.value:
                ns.value = x
                ns.lower[:] = [(I,J)]
            elif x == ns.value:
                ns.lower.append((I,J))

    # N, W, E, S, x
    direction = np.zeros(data.shape, dtype=object)
    for i in range(H):
        for j in range(W):
            ns.value = data[i,j]
            ns.lower = []
            try_dir(-1,0)
            try_dir(0,-1)
            try_dir(0,1)
            try_dir(1,0)
            if ns.value == data[i,j]:
                direction[i,j] = (0,0)
            else:
                direction[i,j] = ns.lower[0]

    #print(direction)
    labels = np.empty(data.shape, dtype=int)
    labels[:] = -1
    apply_numeric_labels(direction, labels)
    #print(labels)
    #return

    alpha = numeric_to_alpha(labels)
    print('\n'.join(' '.join(row) for row in alpha))

def run(filename):
    with open(filename) as f:
        for line in f:
            T = int(line.strip())
            break
        for i in range(1,T+1):
            rows = []
            for line in f:
                H, W = map(int, line.strip().split())
                break
            for line in f:
                rows.append([int(x) for x in line.strip().split()])
                if len(rows) >= H:
                    break
            data = np.array(rows)
            process(i, data)

if __name__ == "__main__":
    try:
        filename, = sys.argv[1:]
    except ValueError:
        print('USAGE: %s filename'%sys.argv[0], file=sys.stderr)
        sys.exit(1)
    run(filename)
