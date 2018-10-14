#!/usr/bin/env python3

T = int(input())
for i in range(T):
    ans1 = int(input())
    board1 = [map(int, input().split()) for j in range(4)]
    row1 = set(board1[ans1 - 1])

    ans2 = int(input())
    board2 = [map(int, input().split()) for j in range(4)]
    row2 = set(board2[ans2 - 1])

    ans = row1 & row2
    if len(ans) == 0:
        print("Case #{}: Volunteer cheated!".format(i + 1))
    elif len(ans) == 1:
        print("Case #{}: {}".format(i + 1, ans.pop()))
    else:
        print("Case #{}: Bad magician!".format(i + 1))
