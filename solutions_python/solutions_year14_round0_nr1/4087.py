#!/usr/bin/env python
import sys
def main():
    T = int(sys.stdin.readline())
    for case in range(1,T+1):
        doCase(case)
def doCase(case):
    answer = int(sys.stdin.readline())
    row = getLine(answer-1)
    answer = int(sys.stdin.readline())
    another_row = getLine(answer-1)
    card = []
    for n in row:
        if n in another_row:
            card.append(n)
    if len(card) == 0:
        print("Case #{}: Volunteer cheated!".format(case))
    if len(card) == 1:
        print("Case #{}: {}".format(case, card[0]))
    if len(card) > 1:
        print("Case #{}: Bad magician!".format(case))
def getLine(num):
    line = []
    for i in range(0,4):
        if i == num:
            line = sys.stdin.readline().split()
        else:
            sys.stdin.readline()
    line = [int(i) for i in line]
    return line

if __name__ == '__main__':
        main()
