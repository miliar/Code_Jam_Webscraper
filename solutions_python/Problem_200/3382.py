#!/usr/bin/env python

import sys


def tidy(N):
    size = len(N)
    if size == 1:
        return N
    idx = 0
    temp = ""

    # forward pass
    while idx < size - 1:
        if N[idx] <= N[idx+1]:
            temp += N[idx]
            idx += 1
        else:
            temp += str(int(N[idx])-1)
            idx += 1
            break

    if (idx == size - 1) and (N[idx] >= N[idx-1]):
        return N
    nines = "9"*(size-idx)

    output = ""
    value = temp[-1]
    idx -= 1
    # backward pass
    while idx > 0:
        if temp[idx-1] > value:
            output = "9" + output
            value = str(int(temp[idx-1])-1)
        else:
            output = value + output
            value = temp[idx-1]
        idx -= 1

    output = value + output + nines
    return output.lstrip("0")


def print_result(i, output):
    print("Case #{}: {}".format(i, output))


def main():
    a = int(sys.stdin.readline())
    for i in range(1, a+1):
        line = sys.stdin.readline().split()
        N = line[0]
        output = tidy(N)
        print_result(i, output)


if __name__ == '__main__':
    main()
