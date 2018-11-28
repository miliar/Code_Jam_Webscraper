#!/usr/bin/env python

from itertools import cycle
import sys

def print_solution(answer, case):
    print "Case #%d: %d" % (case, answer)

def solve(R, k, G, case):

    groups = [[i, -1, -1] for i in G]
    total_groups = len(G)
    the_sum = 0
    total = 0
    passengers = 0
    i = 0
    for r in range(R):
        start = i
        if groups[i][1] != -1:
            the_sum += groups[i][1]
            i = groups[i][2]
            continue
            
        while True:
            next_element = groups[i]
            i = (i + 1) % total_groups

            if total + next_element[0] > k:
                the_sum += total
                i = (i - 1) % total_groups
                groups[start][1] = total
                groups[start][2] = i
                total = 0
                break
            elif start == i:
                the_sum += total + next_element[0]
                groups[start][1] = total + next_element[0]
                groups[start][2] = i
                total = 0
                break
            else:
                total += next_element[0]

    print_solution(the_sum, case)

def main():
    cases = []
    T = int(sys.stdin.readline())
    for i in range(1, T + 1):
        R, k, N = (int(j) for j in sys.stdin.readline().split(' '))
        G = [int(j) for j in sys.stdin.readline().split(' ')]
        solve(R, k, G, i)

if __name__ == '__main__':
    main()

