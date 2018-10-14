#! /usr/bin/env python
# code.py (@DESC@)
# Maintainer: Matias Larre Borges <matias@larre-borges.com>
# Last Change: 2009 Sep 13

import sys

cells = []
possible_answers = []

def count_prisoners_left(l):
    res = 0
    for i in range(l-1, -1, -1):
        if cells[i] != 0:
            res += 1
        else:
            break
    return res

def count_prisoners_right(l):
    res = 0
    for i in range(l+1, len(cells)):
        if cells[i] != 0:
            res += 1
        else:
            break
    return res

def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

def main():
    file = open(sys.argv[1])

    nb_cases = int(file.readline())

    for case_nb in range(1, nb_cases + 1):

        P, Q = [int(x) for x in file.readline().split(' ')]

        global possible_answers

        liberation_order = [int(x) for x in file.readline().split(' ')]

        best_answer = 9999999999999999999

        for p in all_perms(liberation_order):
            global cells
            cells = [1 for x in range(P)]
            gold_coins = 0
            good = True
            for l in p:
                cells[l-1] = 0
                gold_coins += count_prisoners_left(l-1)
                gold_coins += count_prisoners_right(l-1)
                if gold_coins > best_answer:
                    good = False
                    break
            if good:
                best_answer = gold_coins
            else:
                continue

        print "Case #%d: %d" % (case_nb, best_answer)

    file.close()


if __name__ == "__main__":
    main()
