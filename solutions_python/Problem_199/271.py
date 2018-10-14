#!/usr/bin/env python3

from collections import deque

def calc(s, k):
    c = 0
    while len(s) >= k:
        first = s.popleft()
        if first == 0:
            for i in range(k-1):
                s[i] = 1 - s[i]
            c += 1
    return c if s == deque([1] * (k-1)) else 'IMPOSSIBLE'

def main():
    t = int(input())
    for i in range(t):
        s, k = input().split()
        s = deque([(1 if c == '+' else 0) for c in s])
        k = int(k)
        r = calc(s, k)
        print('Case #{}: {}'.format(i+1, r))

if __name__ == '__main__':
    main()
