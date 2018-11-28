#!/usr/bin/env python

def solve():
    N, K = raw_input().split()
    N = int(N)
    K = int(K)
    U = float(raw_input())
    Pi = map(float, raw_input().split())

    sorted_Pi = sorted(Pi)

    while(U > 0):
        index = 0

        if (N == 1):
            sorted_Pi[0] += U
            U = 0
            continue

        if (sorted_Pi[index] < sorted_Pi[index + 1]):
            if (U >= sorted_Pi[index + 1] - sorted_Pi[index]):
                U -= sorted_Pi[index + 1] - sorted_Pi[index]
                sorted_Pi[index] += sorted_Pi[index + 1] - sorted_Pi[index]
                continue
            else:
                sorted_Pi[index] += U
                U = 0
                continue

        index += 1
        while ((index < N - 1) and (sorted_Pi[index] == sorted_Pi[index + 1])):
            index += 1

        if (index == N - 1):
            add = U / float(index + 1)
            for idx in xrange(index + 1):
                sorted_Pi[idx] += add
            U = 0
            continue

        # We now have the number of equal indices, and we're going to split U
        if (U >= (index + 1) * (sorted_Pi[index + 1] - sorted_Pi[index])):
            U -= (index + 1) * (sorted_Pi[index + 1] - sorted_Pi[index])
            for idx in xrange(index + 1):
                sorted_Pi[idx] += sorted_Pi[index + 1] - sorted_Pi[index]
        else:
            add = U / float(index + 1)
            for idx in xrange(index + 1):
                sorted_Pi[idx] += add
            U = 0

    mult = 1
    for idx in xrange(N):
        mult *= sorted_Pi[idx]

    return mult

def main():
    T = int(raw_input())
    for t in xrange(T):
        print "Case #{}: {}".format(t + 1, solve())


if __name__ == '__main__':
    main()
