#!/usr/bin/env python3
"""
The Repeater problem
for Google Code Jam 2014
Round 1B

Link to problem description:
https://code.google.com/codejam/contest/2994486/dashboard#s=p0

author: 
Christos Nitsas
(chrisn654 or nitsas)

language:
Python 3(.3)

date:
May, 2014

usage:
$ python3 runme.py sample.in
or
$ runme.py sample.in
(where sample.in is the input file and $ the prompt)
"""


import sys
import operator
# non-standard modules:
from helpful import read_int


# SDF (Stripped Down Form) functions:


def sdf(word):
    stripped = []
    for ch in word:
        try:
            if stripped[-1] == ch:
                continue
        except IndexError:
            pass
        stripped.append(ch)
    return "".join(stripped)


def have_same_sdf(words):
    first_sdf = sdf(words[0])
    for word in words[1:]:
        if sdf(word) != first_sdf:
            return False
    return True


# PCF (Position Cardinality Form) functions:


def pcf(word):
    cardinalities = []
    cardinality = 1
    pre_ch = word[0]
    for ch in word[1:]:
        if ch == pre_ch:
            cardinality += 1
        else:
            cardinalities.append(cardinality)
            cardinality = 1
            pre_ch = ch
    cardinalities.append(cardinality)
    return cardinalities


def mean_of_pcfs(pcfs):
    mean_pcf = [0] * len(pcfs[0])
    for pcf in pcfs:
        for i, c in enumerate(pcf):
            mean_pcf[i] += c
    for i in range(len(mean_pcf)):
        mean_pcf[i] = round(mean_pcf[i]/len(pcfs))
    return mean_pcf


def distance(pcf, target):
    result = sum(abs(pi - ti) for pi, ti in zip(pcf, target))
    return result


# Main functions:


def solve(words):
    if not have_same_sdf(words):
        return "Fegla Won"
    # all the words have the same stripped down form
    # i.e. Omar can win - we only need to calculate the minimum 
    # number of moves
    pcfs = [pcf(word) for word in words]
    mean_pcf = mean_of_pcfs(pcfs)
    min_moves = sum(distance(pcf, mean_pcf) for pcf in pcfs)
    return min_moves


def main(filename=None):
    if filename is None:
        if len(sys.argv) == 2:
            filename = sys.argv[1]
        else:
            print("Usage: runme.py input_file")
            return 1
    with open(filename, "r") as f:
        T = read_int(f)
        test_cases = []
        for i in range(1, T+1):
            N = read_int(f)
            test_cases.append([f.readline().rstrip() for j in range(N)])
    for i, tc in enumerate(test_cases, start=1):
        print("Case #{}: {}".format(i, solve(tc)))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

