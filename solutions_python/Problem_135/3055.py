#!/usr/bin/env python

import sys

def main():
    case = 1
    first_row = []
    second_row = []
    intersect = []

    inputfile = open(sys.argv[1])
    outfile = open("output.txt", "w")

    inputfile.next()  # Skip number of cases

    for line in inputfile:

        count = int(line)
        for idx in range(0, count):
            first_row = inputfile.next().split()

        for idx in range(0, 4 - count):
            inputfile.next()

        count = int(inputfile.next())
        for idx in range(0, count):
            second_row = inputfile.next().split()

        for idx in range(0, 4 - count):
            inputfile.next()

        intersect = list(set(first_row) & set(second_row))

        if len(intersect) == 1:
            msg = "Case #{}: {}\n".format(case, intersect[0])
        elif len(intersect) > 1:
            msg = "Case #{}: Bad magician!\n".format(case)
        else:
            msg = "Case #{}: Volunteer cheated!\n".format(case)

        outfile.write(msg)
        case += 1

if __name__ == "__main__":
    main()
