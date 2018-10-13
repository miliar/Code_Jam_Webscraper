import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def revert(c):
    if (c == '+'):
        return '-'
    return '+'

def revertPancake(row, size, i):
    if i + size > len(row):
        return row
    row = list(row)
    for j in range(size):
        row[i+j] = revert(row[i+j])
    row = ''.join(row)
    return row




def algo(row, size, case):
    count = 0
    for i in range(0, len(row)):
        if (row[i] == '-'):
            row = revertPancake(row, size, i)
            count += 1
    if '-' not in row:
        print('Case #' + str(case+1) + ":", count)
    else:
        print('Case #'+ str(case+1) + ": IMPOSSIBLE")


def main():
    n = int(input())
    for i in range(n):
        row, size = input().split()
        algo(row, int(size), i)

main()