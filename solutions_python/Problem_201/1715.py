import sys
from collections import Counter

sys.stdin = open(sys.argv[1], 'r')

def f():
    n, k = map(int, input().split())
    sizes = Counter()
    sizes[n] = 1

    while k > 0:
        size = max(sizes)
        count = sizes.pop(size)
        l = (size - 1) // 2
        r = (size - 1) // 2 + ((size - 1) % 2)
        sizes[l] += count
        sizes[r] += count

        k -= count

    return str(r) + " " + str(l)

for t in range(1, int(input()) + 1):
    print("Case #%d:" % t, f())