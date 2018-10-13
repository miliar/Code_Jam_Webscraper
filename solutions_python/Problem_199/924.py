#!/usr/bin/env python

INFILE='/Users/linlin/Downloads/A-small-attempt1.in'

def flip(pc, num):
    if '-' not in pc:
        return 0
    else:
        pc = pc[pc.index('-'):]
        if num > len(pc):
            return 'IMPOSSIBLE'
    for i in range(num):
        if pc[i] == '-':
            pc[i] = '+'
        else:
            pc[i] = '-'
    if '-' in pc:
        newpc = pc[pc.index('-'):]
    else:
        newpc = ''
    if num <= len(newpc):
        left = flip(newpc, num)
        if left == 'IMPOSSIBLE':
            return left
        else:
            return 1 + left
    else:
        if '-' in newpc:
            return 'IMPOSSIBLE'
        else:
            return 1 

def process(input):
    pc, num = input.split()
    result = flip(list(pc), int(num))
    return result

def raw_input(path, ignore_num=True):
    result = []
    with open(path, 'r') as inf:
        if ignore_num:
            inf.readline()
        for line in inf:
            result.append(line.strip())
    return result

def run(input):
    i = 1
    for line in input:
        output = process(line)
        print "Case #%d: %s" % (i, str(output))
        i += 1

if __name__ == '__main__':
    run(raw_input(INFILE))
