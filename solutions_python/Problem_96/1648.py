#!/usr/bin/python
import sys

# Dancing With the Googlers

def get_input_lines(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    n = int(lines[0])
    return lines[1:n+1]

def main(infile):
    lines = get_input_lines(infile)
    for i, line in enumerate(lines):
        input = [int(x) for x in line.split()]
        n, s, p = input[:3]
        totals = input[3:]
        normals, specials = [0, 0]
        for t in totals:
            l = t / 3
            d = t % 3
            if d == 0:
                if l >= p:
                    normals += 1
                elif l == p - 1 and t > 1:
                    specials += 1
            elif d == 1:
                if l >= p - 1:
                    normals += 1
            elif d == 2:
                if l >= p - 1:
                    normals += 1
                elif l == p - 2:
                    specials += 1
        final = 0
        if s > specials:
            final = s + (normals - (s - specials))
        else:
            final = s + normals
        print("Case #%u: %u" % (i + 1, final))

main(sys.argv[1])
