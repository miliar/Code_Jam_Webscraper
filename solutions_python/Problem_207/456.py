#!/usr/bin/env python3
# -*- coding: utf-8 -*-


T = int(input())  # number of test cases
for t in range(T):
    N, R, O, Y, G, B, V = [int(v) for v in input().split()]  # total, per color

    # small
    colors = [[R, 'R'], [Y, 'Y'], [B, 'B']]
    colors.sort()
    if colors[2][0] > colors[1][0] + colors[0][0]:
        ans = 'IMPOSSIBLE'
    else:
        ans = list()
        col = colors[-1][1]
        colors[-1][0] -= 1
        ans.append(col)
        for i in range(1, N):
            colors.sort()
            temp = colors[-1][1]
            if temp == col:
                temp = colors[-2][1]
                colors[-2][0] -= 1
            else:
                colors[-1][0] -= 1
            col = temp
            ans.append(col)
        if ans[0] == ans[-1]:
            a, b = ans[-2:]
            ans[-1] = a
            ans[-2] = b
        ans = ''.join(ans)
        # recheck
        fail = False
        for i in range(N - 1):
            if ans[i] == ans[i + 1]:
                fail = True
                print(i, i + 1)
        if ans[0] == ans[-1]:
            fail = True
            print('end')
            print(colors)
            print(R, Y, B)
        if fail:
            print(ans)
            raise Exception
    print("Case #{:d}: {:s}".format(t + 1, ans))
