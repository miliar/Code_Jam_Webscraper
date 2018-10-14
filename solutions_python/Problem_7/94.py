#!/usr/bin/env python2.5

"""
Google Code Jam 2008
Solution for the "Crop Triangles" problem.
rbp@isnomore.net

Usage: triangles.py input_file output_file
"""

import sys

def read_input():
    in_file = file(sys.argv[1])

    in_text = in_file.readlines()
    n_cases = int(in_text.pop(0))
    cases = []
    for i in range(n_cases):
        c = {}
        n, A, B, C, D, x0, y0, M = [int(j) for j in in_text.pop(0).split()]
        c['n'] = n
        c['A'] = A
        c['B'] = B
        c['C'] = C
        c['D'] = D
        c['x0'] = x0
        c['y0'] = y0
        c['M'] = M
        cases.append(c)
    in_file.close()
    return cases

def coordinates(c):
    x = c['x0']
    y = c['y0']
    yield (x, y)
    for i in range(1, c['n']):
        x = (c['A'] * x + c['B']) % c['M']
        y = (c['C'] * y + c['D']) % c['M']
        yield (x, y)

def center(v1, v2, v3):
    return ((v1[0] + v2[0] + v3[0])/3.0 +
            (v1[1] + v2[2] + v3[3])/3.0)

def exact_center(v1, v2, v3):
    return ((v1[0] + v2[0] + v3[0]) % 3 == 0 and
            (v1[1] + v2[1] + v3[1]) % 3 == 0)
    
def triangle_combinations(points, n=3):
    if n == 0:
        yield []
    else:
        for i in xrange(len(points)):
            for c in triangle_combinations(points[i+1:], n-1):
                yield [points[i]] + c

def solve_case(c):
    triangles = 0
    coords = list(coordinates(c))
    #print coords
    for a, b, c in triangle_combinations(coords):
        #print a, b, c
        if exact_center(a, b, c):
            triangles += 1
    return triangles

if __name__ == '__main__':
    cases = read_input()
    #print cases
    output = "\n".join(['Case #%d: %d' % (i+1, solve_case(c))
                        for i, c in enumerate(cases)])
    if len(sys.argv) < 3:
        print output
    else:
        out_file = file(sys.argv[2], "w")
        out_file.write(output)
        out_file.close()
