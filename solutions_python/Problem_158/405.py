#!/usr/bin/env python

def get_winner(X, R, C):
    winning_cases = {2: [(1, 2), (2, 1), (1, 4), (4, 1), (2, 2), (2, 3), (3, 2), (2, 4), (4, 2), (3, 4), (4, 3), (4, 4)],
                    3: [(2, 3), (3, 2), (3, 3), (3, 4), (4, 3)],
                    4: [(3, 4), (4, 3), (4, 4)]
                   }

    if X == 1 or (R, C) in winning_cases[X]:
        return 'GABRIEL'
    else:
        return 'RICHARD'



if __name__ == '__main__':
    T = int(raw_input())
    for t in range(1, T + 1):
        X, R, C = map(int, raw_input().split())
        print 'Case #%d: %s' % (t, get_winner(X, R, C))
