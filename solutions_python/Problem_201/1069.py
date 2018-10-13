from heapq import *


def inp():
    cases = []
    t = int(input())
    for i in range(t):
        n, k = [int(x) for x in input().split()]
        cases.append((n, k))
    return cases


def process(n, k):
    a = [-n]
    for i in range(k-1):
        t = heappop(a)
        heappush(a, t // 2 + 1)
        if t % 2 == 0:
            heappush(a, t // 2)
        else:
            heappush(a, t // 2 + 1)
    last = heappop(a)
    if last % 2 == 0:
        return abs(last) // 2, abs(last) // 2 - 1
    else:
        return abs(last) // 2, abs(last) // 2


def main():
    cases = inp()
    for i in range(len(cases)):
        print("Case #{}: {} {}".format(i+1, *process(*cases[i])))

if __name__ == '__main__':
    main()
