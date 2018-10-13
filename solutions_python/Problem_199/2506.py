#!/usr/bin/env python3


def solveOne(case):
    """ Solve a single testcase `case` """
    def swapK(arr, pos, span):
        for i in range(pos, pos+span):
            arr[i] = not arr[i]
        return arr

    pancakes, span = input().strip().split(' ')
    span = int(span)
    pancakes = [x == '+' for x in pancakes]
    swaps = 0
    for pos in range(len(pancakes) - span + 1):
        if not pancakes[pos]:
            swaps += 1
            pancakes = swapK(pancakes, pos, span)

    for x in pancakes:  # Overkill but easier
        if not x:
            return "IMPOSSIBLE"
    return swaps


if __name__ == '__main__':
    numCases = int(input())
    for case in range(1, numCases+1):
        print("Case #{}: {}".format(case, solveOne(case)))
