import sys
import math
sys.stdin = open('input.in', 'r')
sys.stdout = open('output.out', 'w')


def length(k, n):
    if k == 1:
        return n

    lengthParent = length(k // 2, n)

    if k % 2 == 0:
        return lengthParent - (lengthParent - 1) // 2 - 1

    return (lengthParent - 1) // 2


def output(n, k):
    d = math.floor(math.log2(k))
    elem = int(math.pow(2, d))

    node = elem

    while k > 1:
        if k % 2 != 0:
            node += elem // 2

        d -= 1
        elem //= 2
        k //= 2

    l = length(node, n)

    lengthShort = (l - 1) // 2
    lengthLong = l - lengthShort - 1

    return str(lengthLong) + " " + str(lengthShort)

T = int(input())

for i in range(T):
    [N, K] = input().split(" ")
    N = int(N)
    K = int(K)
    print("Case #" + str(i+1) + ": " + str(output(N, K)))
