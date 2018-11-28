#!/usr/bin/env python

def get_min_eaten(m):
   
    first_min = 0
    for i in range(1, len(m)):
        if m[i] < m[i- 1]:
            first_min += m[i - 1] - m[i]

    rate = 0
    for i in range(1, len(m)):
        rate = max(rate, m[i -1] - m[i])

    second_min = 0
    for i in range(len(m) - 1):
        if m[i] < rate:
            second_min += m[i]
        else:
            second_min += rate

    return first_min, second_min
        

if __name__ == '__main__':
    T = int(raw_input())
    for t in range(1, T + 1):
        N = int(raw_input())
        m = map(int, raw_input().split())
        res = get_min_eaten(m)
        print 'Case #%d: %d %d' % (t, res[0], res[1])
