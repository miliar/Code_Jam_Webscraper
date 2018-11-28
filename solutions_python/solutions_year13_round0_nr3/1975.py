#!/usr/bin/env python

import math
import fileinput

def is_fair(current):
    current_lst = list(str(current))
    current_length = len(current_lst)
    i = 0
    j = current_length - 1
    while i <= j:
        if current_lst[i] is not current_lst[j]:
            return False
        j -= 1
        i += 1
    return True

def is_square(current):
    x = int(math.sqrt(current))
    return current - (x * x) is 0

def is_canonical(current):
    while is_fair(current):
        if is_square(current):
            current = int(math.floor(math.sqrt(current)))
            if is_fair(current):
                return True
        else:
            return False
    return False


def fair_square(start, end):
    current = start
    results = []
    while current <= end:
        if is_canonical(current):
            results.append(current)
        current += 1
    return results

current_case = 0
current_line = 0
for line in fileinput.input():
    line = line.strip()
    current_line += 1
    if current_line is 1:
        continue
    current_case += 1
    dim = line.split(" ")
    assert len(dim) is 2
    start = int(dim[0])
    end = int(dim[1])
    results = fair_square(start, end)
    print "Case #%d: %d" % (current_case, len(results))
