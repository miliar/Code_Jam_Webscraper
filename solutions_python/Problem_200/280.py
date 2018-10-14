#!/usr/bin/env python3

from collections import deque

def calc(n):
    b = 0
    i = 0
    while i < len(n)-1 and n[i] <= n[i+1]:
        if n[i] < n[i+1]:
            b = i+1
        i += 1
    if i < len(n)-1: # found an unordered pair
        n[b] = str(int(n[b]) - 1)
        for j in range(b+1, len(n)):
            n[j] = '9'
    if n[0] == '0':
        return ''.join(n[1:])
    else:
        return ''.join(n)

def main():
    t = int(input())
    for i in range(t):
        n = list(input().strip())
        r = calc(n)
        print('Case #{}: {}'.format(i+1, r))

if __name__ == '__main__':
    main()
