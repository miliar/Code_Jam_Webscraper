#!/usr/bin/python

import re
import sys

input_file = open('A-large.in')
output_file = open('A-large.out', 'w')
#output_file = sys.stdout

T = int(input_file.readline())

def get_number_mkdirs(m, ns):
    lowest_number = len(m)
    for existing_parts in ns:
        i = 0
        while i < len(m):
            if i == len(existing_parts) or m[i] != existing_parts[i]:
                break
            i += 1


        if len(m) - i < lowest_number or lowest_number == -1:
            lowest_number = len(m) - i

    return lowest_number



for t in range(T):
    (N, M) = map(int, input_file.readline().split(' '))
    ns = []
    for n in range(N):
        ns.append(input_file.readline().lstrip('/').rstrip('\n').split('/'))
#    reduce(ns)
    ms = []
    for m in range(M):
        ms.append(input_file.readline().lstrip('/').rstrip('\n').split('/'))

    result = 0
    for m in ms:
        result += get_number_mkdirs(m, ns)
        ns.append(m)
#        reduce(ns)

    output_file.write("Case #" + str(t + 1) + ": " + str(result) + "\n")

input_file.close()
output_file.close()
