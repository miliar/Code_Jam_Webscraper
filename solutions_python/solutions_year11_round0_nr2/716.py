#!/usr/bin/python2 
from __future__ import print_function

def apply_f(s, l):
    for elem in l:
        r = elem.apply(s)
        if r != None:
            return r

    return None

with open("input.txt") as f:
    lines = f.readlines()
    lines.pop(0)
    n_line = 0
    for line in lines:
        n_line += 1
        line_split = line.split()

        n_combines = int(line_split.pop(0))
        combines = line_split[:n_combines]
        line_split = line_split[n_combines:]

        n_opposed = int(line_split.pop(0))
        opposedes = line_split[:n_opposed]
        line_split = line_split[n_opposed:]

        line_split.pop(0)

        if len(line_split) != 1:
            raise Exception("Wrong line %d" % n_line)

        s = line_split.pop(0)

        magic = []
        for letter in s:
            magic.append(letter)
            if len(magic) <= 1:
                continue

            for combine in combines:
                if (set(combine[:2]) == set(magic[-2:])):
                    magic = magic[:-2]
                    magic.append(combine[2])
                    break;

            for opposed in opposedes:
                if (set(magic).issuperset(set(opposed))):
                    magic = []
                    break;

        s_magic = ""

        for letter in magic:
            s_magic += letter + ', '

        s_magic = s_magic[:-2]
        
        print("Case #%d: [%s]" % (n_line, s_magic))
