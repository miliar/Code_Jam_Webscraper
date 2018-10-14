#!/usr/bin/env python3

def pop(state, k, n):
    state[k] -= n
    if state[k] == 0:
        state.pop(k)

def add(state, k, n):
    state.setdefault(k, 0)
    state[k] += n

def solve(n, k):
    state = {n: 1}
    while k > 1:
        s = max(state.keys())
        c = min(state[s], k - 1)
        a, b = int(s / 2), int((s - 1) / 2)
        pop(state, s, c)
        add(state, a, c)
        add(state, b, c)
        k -= c

    s = max(state.keys())
    a, b = int(s / 2), int((s - 1) / 2)
    return (a, b)

if __name__ == "__main__":
    t = int(input())
    for i in range(1, t + 1):
        print("Case #{}: {} {} ".format(i, *solve(*map(int, input().split()))))
