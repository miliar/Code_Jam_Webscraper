#!/usr/bin/env python

T = int(raw_input())
for testCaseIndex in range(T):
    row1index = int(raw_input())
    board1 = list()
    for i in range(0, 4):
        board1.append(list(int(s) for s in raw_input().split(' ')))
    row2index = int(raw_input())
    board2 = list()
    for i in range(0, 4):
        board2.append(list(int(s) for s in raw_input().split(' ')))
    
    row1 = board1[row1index - 1]
    row2 = board2[row2index - 1]
    results = list(set(row1) - (set(row1) - set(row2)))

    if len(results) == 1:
        print 'Case #{0:d}: {1:d}'.format(testCaseIndex + 1, results[0])
    elif len(results) > 1:
        print 'Case #{0:d}: Bad magician!'.format(testCaseIndex + 1)
    else:
        print 'Case #{0:d}: Volunteer cheated!'.format(testCaseIndex + 1)
