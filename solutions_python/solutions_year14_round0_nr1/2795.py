#!/usr/bin/env python
import fileinput
import sys


def find_card(rows1, rows2, answer1, answer2):
    return set(rows1[answer1]).intersection(set(rows2[answer2]))


def main():

    infile = fileinput.input()
    numCases = int(infile.readline())

    for case in range(1, numCases+1):
        sys.stdout.write("Case #{}: ".format(case))
        answer1 = int(infile.readline()) - 1
        rows1 = []
        rows2 = []
        for x in range(0, 4):
            rows1.append(infile.readline().strip().split())
        answer2 = int(infile.readline()) - 1
        for x in range(0, 4):
            rows2.append(infile.readline().strip().split())

        intersection = find_card(rows1, rows2, answer1, answer2)

        if len(intersection) < 1:
            print "Volunteer cheated!"
        elif len(intersection) > 1:
            print "Bad magician!"
        else:
            print intersection.pop()

if __name__ == "__main__":
    main()
