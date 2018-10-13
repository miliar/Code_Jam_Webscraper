#!/usr/bin/env python3
import sys

def solve(row1,row2):
    counter = 0
    card = 0
    for x in row1:
        if x in row2:
            card = x
        else:
            counter += 1
    if counter == 3:
        return str(card)
    elif counter == 4:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"

def main(filename):
    with open(filename, 'r') as f:
        testcases = int(f.readline())
        for case_num in range(testcases):
            answer1 = int(f.readline()) - 1
            row1 = []
            for x in range(4):
                line = f.readline()
                if x == answer1:
                    row1 = [int(c) for c in line.split()]

            answer2 = int(f.readline()) - 1
            row2 = []
            for x in range(4):
                line = f.readline()
                if x == answer2:
                    row2 = [int(c) for c in line.split()]

            print("Case #{0}: {1}".format(case_num + 1, solve(row1,row2)))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
