from __future__ import print_function, division
from fileinput import input

inp = input()
t = int(inp.readline())


def first_dec(l):
    for i in xrange(len(l) - 1):
        if l[i] > l[i+1]:
            return i
    return -1


def solve(n):
    number = [0] + [int(x) for x in str(n)]
    index = first_dec(number)
    if index == -1:
        return int("".join(str(x) for x in number))
    cur = number[index]
    for i in xrange(index, 0, -1):
        if number[i] == cur:
            true_index = i
        else:
            break
    number[true_index] -= 1
    for ind in xrange(true_index + 1, len(number)):
        number[ind] = 9
    return int("".join(str(x) for x in number))

for case in xrange(t):
    n = int(inp.readline())
    print("Case #{}: {}".format(case + 1, solve(n)))
