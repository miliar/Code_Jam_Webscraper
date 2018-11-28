from __future__ import with_statement
import re

def create_pattern(input):
    buff = ""
    in_class = False
    for char in input:
        if char not in "()":
            buff += char
        elif char == "(":
            buff += char
            in_class = True
            continue
        else:
            buff = buff[:-1] + char
            in_class = False
            continue
        if in_class:
            buff += "|"
    return re.compile(buff)

with open("A-large.in.txt") as f:
    lines = [l[:-1] for l in f.readlines()]
    L,D,N = [int(x) for x in lines[0].split(" ")]
    words = lines[1:D + 1]
    patterns = [create_pattern(x) for x in lines[D + 1:D + N + 1]]
    for i, pattern in enumerate(patterns):
        cur_case = 0
        for word in words:
            if pattern.match(word):
                cur_case += 1
        print "Case #%i: %i" %(i + 1, cur_case)
