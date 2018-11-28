#!/usr/bin/python3

import sys
import math

def game(armin, others, nb_steps=0):
    

    while True:
        smallers = [s for s in others if s < armin]
        others = [s for s in others if s >= armin]
        armin += sum(smallers)

        if len(smallers) == 0:
            break

    if len(others) == 0:
        return nb_steps

    if armin != 1:
        s2 = game(armin * 2 - 1, others, nb_steps + 1)
    else:
        s2 = None
    s1 = game(armin, others[:-1], nb_steps + 1)

    if s2 == None:
        return s1

    if s1 < s2:
        return s1
    else:
        return s2

def main():
    nb = int(f.readline().strip())
    for case_id in range(1, nb + 1):
        l = f.readline().strip()
        sizes = l.split(' ')
        armin = int(sizes[0])
        nb_motes = int(sizes[1])

        l = f.readline().strip()
        others = [int(x) for x in l.split(' ')]
        others.sort()

        steps = game(armin, others)

        print('Case #%d: %d' % (case_id, steps), file = o)
        case_id += 1
    
def open_files():
    if len(sys.argv) == 1:
        f = sys.stdin
        o = sys.stdout

    if len(sys.argv) == 2:
        f = open(sys.argv[1], 'r')
        o = sys.stdout

    if len(sys.argv) == 3:
        f = open(sys.argv[1], 'r')
        o = open(sys.argv[2], 'w')

    return (f, o)


(f, o) = open_files()
main()


