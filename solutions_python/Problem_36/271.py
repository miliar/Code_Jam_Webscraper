#!/usr/bin/env python
# -*- coding: utf-8 -*-

STRING = 'welcome to code jam'

class CannotIncAnymore(Exception):
    '''I cannot increment the index list anymore. Sorry.'''

def str_eq(input, indices, string):
    prod = ''
    for index in indices:
        prod += input[index]
    return prod == string

def beautify(input):
    input = str(input)
    if len(input) >= 4:
        return input[-4] + input[-3] + input[-2] + input[-1]
    else:
        return input.zfill(4)

def can_inc(i, indices, input):
    pos = input.find(STRING[i], indices[i]+1)
    if pos == -1:
        return False
    else:
        if pos + len(indices) - i > len(input):
            return False
    return True

def inc(idxs, input):
    zeroes = []
    indices = [i for i in idxs]
    for i in range(len(indices) - 1, -1, -1):
        if can_inc(i, indices, input):
            indices[i] = input.find(STRING[i], indices[i]+1)
            break
        else:
            zeroes.append(i)
    if len(zeroes) == len(indices) or 0 in zeroes:
        raise CannotIncAnymore
    else:
        zeroes.reverse()
        for i in zeroes:
            indices[i] = indices[i-1] + 1
        return indices

def solve(input):
    indices = []
    count = 0

    if len(input) < len(STRING):
        return 0

    it = 0
    pos = 0
    while len(indices) < len(STRING):
        indices.append(input.find(STRING[it], pos))
        pos = indices[it]
        it += 1

    try:
        while True:
            if str_eq(input, indices, STRING):
                count += 1
            indices = inc(indices, input)
    except CannotIncAnymore:
        return count

if __name__ == '__main__':
    N = int(raw_input())
    for i in range(N):
        input = raw_input()
        count = solve(input)
        print 'Case #%d: %s' % (i+1, beautify(count))

