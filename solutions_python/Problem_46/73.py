#! /usr/bin/env python
# code.py (@DESC@)
# Maintainer: Matias Larre Borges <matias@larre-borges.com>
# Last Change: 2009 Sep 26

import sys

def score(line):
    c = len(line)
    for d in range(len(line) - 1, 0, -1):
        if line[d] == 1:
            break
        c = c - 1
    return c

def swap(tab, a, b):
    temp = tab[b]
    tab[b] = tab[a]
    tab[a] = temp
    return tab

def swap_from_to(tab, a, b):
    nb_swaps = 0
    for i in range(b, a, -1):
        tab = swap(tab, i, i-1)
        nb_swaps += 1
    return tab,nb_swaps

def main():
    file = open(sys.argv[1])

    nb_cases = int(file.readline())

    for case_nb in range(1, nb_cases + 1):

        lines = int(file.readline())
        M = []
        for i in range(0, lines):
            line = file.readline().replace('\n','')
            M.append(score([int(x) for x in line]) - 1)

        swap_counts = 0
        while (True):
            swapped = False
            for i in range(0, len(M)):
                if M[i] > i: # current line is not in good position
                    # take first line that could go here and move it here
                    for j in range(i+1, len(M)):
                        if M[j] <= i:
                            M,c = swap_from_to(M, i, j)
                            swap_counts += c
                            swapped = True
                            break
            if not swapped:
                break

        print "Case #%d: %d" % (case_nb, swap_counts)

    file.close()


if __name__ == "__main__":
    main()
