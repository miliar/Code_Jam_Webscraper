#!/usr/bin/python

import os
import sys

def main(infile):
    f = open(infile, "r")
    T = int(f.readline()[:-1])
    i = 0
    while i < T:
        ans1 = int(f.readline()[:-1])
        cards1 = []
        for j in range(0, 4):
            cards1.append(map(int, f.readline()[:-1].split(" ")))
        ans2 = int(f.readline()[:-1])
        cards2 = []
        for j in range(0, 4):
            cards2.append(map(int, f.readline()[:-1].split(" ")))
        print "Case #" + str(i+1) + ": " + solve_case(ans1, cards1, ans2, cards2)
        i += 1
    f.close()

def solve_case(ans1, cards1, ans2, cards2):
    # print ans1, cards1, ans2, cards2
    set1 = set(cards1[ans1 - 1])
    set2 = set(cards2[ans2 - 1])
    inters = set1 & set2
    if len(inters) == 1:
        return str(inters.pop())
    if len(inters) == 0:
        return "Volunteer cheated!"
    if len(inters) > 1:
        return "Bad magician!"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main("A-example.in")

