#!/usr/bin/env python

import itertools
import math
import sys

# Global variables
output_file = None
current_case = 1
DEBUG = True


# The main method which will receive a parsed input file
def jam(lines):
    # Generate all palindromes up to the max possible limit once
    palins = [[], [1,2,3,4,5,6,7,8,9]]
    for i in range(2, 5):
        palins.append(k_palindromes(i))

    # Fixed number of lines
    for i in range(1, len(lines), 1):
        a, b = map(int, lines[i].split())
        print_solution(get_fair_palins(palins, a, b))


# Case-specific program
def get_fair_palins(palins, a, b):
    fair = 0
    ai = len("%d" % a)
    bi = len("%d" % b)
    for i in range(ai, bi+1):
        for p in palins[i]:
            if p >= a and p <= b:
                s = math.sqrt(p)
                if s - int(s) == 0:
                    if int(s) in palins[len("%d" % int(s))]:
                        fair += 1
    return fair


def k_palindromes(k):
    # http://stackoverflow.com/questions/10673422/generate-list-of-all-palindromic-numbers-of-3-digits-in-python
    return [sum([n*(10**i) for i,n in enumerate(([x]+list(ys)+[z]+list(ys)[::-1]+[x]) if k%2
                                else ([x]+list(ys)+list(ys)[::-1]+[x]))])
            for x in range(1,10)
            for ys in itertools.permutations(range(10), k/2-1)
            for z in (range(10) if k%2 else (None,))]

# Boilerplate: method for printing a result
def print_solution(solution):
    global current_case
    global output_file
    result = "Case #%d: %s" % (current_case, solution)
    current_case += 1
    output_file.write(result + "\n")
    if DEBUG:
        print result


# Main entry point, parses input and prepares output file
if __name__ == "__main__":
    lines = []
    filename = "%s-%s-%s" % (sys.argv[1], sys.argv[2], sys.argv[3])
    input_file = file(filename + ".in")
    output_file = file(filename + ".out", 'w')

    for line in input_file:
        lines.append(line.rstrip('\n'))

    jam(lines)
