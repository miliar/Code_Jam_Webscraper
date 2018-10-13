#!/usr/bin/python
# -*- coding utf-8 -*-


def solve():
    s, k = input().split()
    k = int(k)
    cnt = 0
    while len(s) >= k:
        if s[0] == '+':
            s = s[1:]
        else:
            cnt += 1
            s = ''.join([('+' if x == '-' else '-') for x in s[1:k]]) + s[k:]
    if s.count('-'):
        return 'IMPOSSIBLE'
    return cnt


def main():
    t = int(input())
    for i in range(t):
        print('Case #%d:' % (i+1), solve())


if __name__ == '__main__':
    main()
