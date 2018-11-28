#!/usr/bin/python
import string
import sys

def getRow(row_nr, infile):
    for i in range(1,5):
        if i==row_nr:
            raw=infile.readline()
        else:
            infile.readline()
    row = set(int(card) for card in raw.split())

    return row


def main():
    infile = open(sys.argv[1], "r")
    outfile = open(sys.argv[1][:-2] + "out", "w")

    for case in range(1, int(infile.readline())+1):
        rows = [getRow(int(infile.readline()), infile) for i in range(2)]

        result = rows[1].intersection(rows[0])

        if not result:
            output = "Volunteer cheated!"
        else:
            if len(result) > 1:
                output = "Bad magician!"
            else:
                output = int(result.pop())

        print("Case #{0}: {1}".format(case, output), file=outfile)

if __name__ == "__main__":
        main()
