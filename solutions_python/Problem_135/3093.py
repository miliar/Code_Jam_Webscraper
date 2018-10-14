#!/usr/bin/env python3

T = int(input())
for i in range(1, T + 1):
    Q1 = int(input())
    grid1 = [input().split(' ') for j in range(4)]

    Q2 = int(input())
    grid2 = [input().split(' ') for j in range(4)]

    answer = list(set(grid1[Q1 - 1]) & set(grid2[Q2 - 1]))
    if len(answer) == 1:
        print('Case #%d: %s' % (i, answer[0]))
    elif len(answer) == 0:
        print('Case #%d: %s' % (i, "Volunteer cheated!"))
    else:
        print('Case #%d: %s' % (i, "Bad magician!"))
