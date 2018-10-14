#-*- coding: utf-8 -*-

import re

input_file = open("A-large.in")
output_file = open("output.out", 'w')

L, D, N = input_file.readline().split()

L = int(L)
D = int(D)
N = int(N)

words = []
patterns = []
for i in range(D):
    words.append(input_file.readline())

print words
for case in range(1, N+1):
    pattern = input_file.readline().replace('(', '[').replace(')', ']')
    pattern = re.compile(pattern)

    matches = 0
    for word in words:
        if pattern.match(word):
            matches += 1

    output_file.write("Case #%s: %s\n"%(case, matches))
