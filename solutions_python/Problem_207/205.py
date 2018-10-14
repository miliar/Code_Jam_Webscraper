#!/usr/bin/env python3


def solve():
    n, r, o, y, g, b, v = map(int, input().split())
    stables = [None] * n
    letters = ["R", "Y", "B"]
    unicorns = [r, y, b]
    if any(x > n/2 for x in unicorns):
        return "IMPOSSIBLE"
    prev = 10
    indices = [0, 1, 2]
    for i in range(n):
        indices.sort(key=lambda x: -unicorns[x] - (0.1*(stables[0] is x)))
        if prev == indices[0]:
            cur = indices[1]
        else:
            cur = indices[0]
        prev = cur
        stables[i] = cur
        unicorns[cur] -= 1
    return "".join(letters[i] for i in stables)


def main():
    k = int(input())
    for i in range(k):
        print("Case #{}: {}".format(i + 1, solve()))

if __name__ == '__main__':
    main()
