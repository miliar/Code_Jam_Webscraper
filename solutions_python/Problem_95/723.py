# -*- coding: utf-8 -*-

import sys


M = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}


input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[2], 'w')

input_file.readline()

for i, s in enumerate(input_file.readlines()):
    res = []
    for x in s.strip():
        res.append(M[x])
    output_file.writelines("Case #{0}: {1}\n".format(i+1, ''.join(res)))

