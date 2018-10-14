import os
import sys


def calc(x):
    if len(x) == 1:
        return x
    first_dec = -1
    for i in range(len(x) - 1):
        if x[i+1] < x[i]:
            first_dec = i
            break
    if first_dec < 0:
        return x

    start = 0
    for i in range(len(x)):
        if x[i] == x[first_dec]:
            start = i
            break

    ret = x[0:start]
    if start != 0 or x[start] != '1':
        ret += str(int(x[start]) - 1)
    ret += '9' * (len(x) - start - 1)
    return ret


if __name__ == "__main__":
    with open('B-large.in', 'r') as f:
        n = int(f.readline())
        for i in range(n):
            print("Case #%d: %s" % (i+1, calc(f.readline().strip())))
