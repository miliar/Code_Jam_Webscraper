from heapq import nlargest
from math import pi


def top_surf(r):
    return pi * (r ** 2.0)


def A(stack, n, k):
    max_surf = 0
    stack.sort(key=lambda x: x[0], reverse=True)
    sides = [2.0 * pi * r * h for (r, h) in stack]
    for i in range(n - k + 1):
        max_surf = max(max_surf, top_surf(stack[i][0]) + sides[i] + sum(nlargest(k-1, sides[i+1:])))
    return max_surf


def main():
    t = int(raw_input().strip())
    for i in xrange(t):
        n, k = map(int, raw_input().strip().split())
        stack = []
        for _ in range(n):
            stack.append(map(int, raw_input().strip().split()))
        ans = A(stack, n, k)
        print "Case #%s: %.9f" % (i + 1, ans)

if __name__ == '__main__':
    main()
