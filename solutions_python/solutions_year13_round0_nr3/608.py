import sys
from bitarray import bitarray
import math
sys.setrecursionlimit(10000)


def read_ints():
    a = raw_input().split()
    return [int(x) for x in a]


def read_int():
    return read_ints()[0]


def is_palin(x):
    c = str(x)
    for i in range(len(c)/2):
        if c[i] != c[len(c)-i-1]:
            return False
    return True


def solve(inputs):
    max_b = max([val[1] for val in inputs])
    upbound = int(math.sqrt(max_b))
    answer = [0] * len(inputs)

    val = bitarray(upbound)
    val.setall(False)
    val[1] = True
    for i in range(1, upbound+1):
        if is_palin(i):
            val[i] = True
            x = i ** 2
            if x <= max_b and is_palin(x):
                if x < upbound:
                    val[x] = True
                for k in range(len(inputs)):
                    if x >= inputs[k][0] and x <= inputs[k][1]:
                        answer[k] += 1
    for k in range(len(inputs)):
        print 'Case #%d: %d' % (k+1, answer[k])

if __name__ == '__main__':
    T = read_int()
    inputs = []
    for i in range(T):
        inputs.append(read_ints())
    solve(inputs)
