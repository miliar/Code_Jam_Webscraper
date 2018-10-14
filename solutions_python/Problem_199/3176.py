#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(s, k):
    #print '[DEBUG] {}: {}'.format(s, k)
    lens = len(s)
    if lens <= k:
        if s == '+' * lens:
            return 0
        elif s == '-' * lens:
            return 1 if lens == k else -1
        else:
            return -1

    sl = list(s)
    lk = ''.join(sl[0:k])
    if lk == '+' * k:
        ret = solve(''.join(sl[k:]), k)
    else:
        ret1 = -1
        if sl[0] == '+':
            ret1 = solve(''.join(sl[1:]), k)
        for i in xrange(k):
            sl[i] = '-' if sl[i] == '+' else '+'
        if sl[0] == '-':
            ret2 = -1
        else:
            ret2 = solve(''.join(sl[1:]), k)
            if ret2 > -1:
                ret2 += 1

        if ret1 == -1 and ret2 == -1:
            ret = -1
        elif ret1 == -1:
            ret = ret2
        elif ret2 == -1:
            ret = ret1
        else:
            ret = min(ret1, ret2)

    return ret 


def main():
    n = int(raw_input())
    for i in xrange(n):
        S, K = raw_input().split(" ")
        ans = solve(S, int(K))
        if ans == -1:
            ans = 'IMPOSSIBLE'
        print 'Case #{}: {}'.format(i+1, ans)

if __name__ == '__main__':
    main()
