#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pytools import generate_permutations

def compressed_size(string):
    last = ''
    size = 0
    for c in string:
        if c != last:
            size += 1
        last = c
    
    return size

def permute(permutation, string):
    result = ['a'] * len(string)
    for i, p in enumerate(permutation):
        result[i] = string[p]
    return ''.join(result)

def size(k, string):
    minimum = 'inf'
    size = 0
    for permutation in generate_permutations(range(k)):
        result = []
        for i in range(len(string) / k):
            result.append(permute(permutation, string[k*i:k*(i+1)]))
        minimum = min(minimum, compressed_size(''.join(result)))
    return minimum


def test():
    print compressed_size("aaab")

if __name__ == '__main__':
    from sys import argv, exit
    if len(argv) < 2:
        test()
        exit()
    
    file_name = argv[1]
    lines = open(file_name).read().split('\n')[0:-1]
    nb_inputs = int(lines[0])
    lines = lines[1:].__iter__()
    
    for n in range(nb_inputs):
        k = int(lines.next())
        string = lines.next()
        print 'Case #%s:' % (n+1), size(k, string)

