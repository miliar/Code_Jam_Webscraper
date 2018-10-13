#!/usr/bin/env python

def get_min_audience(S):
    cur_audience = S[0]
    audience = 0
    for i in range(1, len(S)):
        if cur_audience < i:
            audience += i - cur_audience
            cur_audience += i - cur_audience
        cur_audience += S[i]
    return audience

if __name__ == '__main__':
    T = int(raw_input())
    for t in range(1, T + 1):
        Smax, S = raw_input().split()
        S = map(int, list(S))
        print 'Case #%d: %d' % (t, get_min_audience(S))
