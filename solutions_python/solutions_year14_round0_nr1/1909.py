#!/usr/bin/env python3

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        r1 = int(input())-1
        m1 = [input().split() for _ in range(4)]
        r2 = int(input())-1
        m2 = [input().split() for _ in range(4)]
        both = list(set(m1[r1]) & set(m2[r2]))
        if not len(both):
            r = 'Volunteer cheated!'
        elif len(both) == 1:
            r = both[0]
        else:
            r = 'Bad magician!'
        print('Case #{}: {}'.format(t, r))
