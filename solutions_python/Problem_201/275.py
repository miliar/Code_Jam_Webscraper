#!/usr/bin/env python3

from collections import deque

def calc(n, k):
    c = 2**(len(bin(k))-3)
    l = (n-k) // c
    return l//2, (l//2 + l%2)

def main():
    t = int(input())
    for i in range(t):
        n, k = input().split()
        l, r = calc(int(n), int(k))
        print('Case #{}: {} {}'.format(i+1, max(l,r), min(l,r)))

if __name__ == '__main__':
    main()
