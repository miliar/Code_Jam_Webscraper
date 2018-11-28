import sys
from collections import defaultdict, Counter
import heapq

# sys.stdin = open('c1.in')
# sys.stdin = open('C-small-1-attempt0.in')
# sys.stdin = open('C-small-2-attempt0.in')
sys.stdin = open('C-large.in')
sys.stdout = open('out.txt', 'w')


def solve_it(n, k):
    h = []
    c = Counter()
    heapq.heappush(h, -n)
    c[n] = 1
    while True:
        i = heapq.heappop(h)
        i *= -1
        l = (i - 1) // 2
        r = i - 1 - l
        for v in [l, r]:
            if v > 0:
                if c[v] == 0:
                    heapq.heappush(h, -v)
                c[v] += c[i]
        k -= c[i]
        c[i] = 0
        if k <= 0:
            break
    max_l = max(l, r)
    min_l = min(l, r)
    res = max_l, min_l
    return res


def main():
    n_cases = int(input())
    for test_case in range(1, n_cases + 1):
        n, k = list(map(int, input().split()))
        print(test_case, file=sys.stderr, end=' ')
        max, min = solve_it(n, k)
        print('Case #' + str(test_case) + ':', max, min)

    print(file=sys.stderr)


if __name__ == '__main__':
    main()
