#!/usr/bin/env pyton
# -*- coding: utf-8 -*-

adjDict = dict()
adjDict['1'] = {'1':'1','i':'i','j':'j','k':'k'}
adjDict['i'] = {'1':'i','i':'-1','j':'k','k':'-j'}
adjDict['j'] = {'1':'j','i':'-k','j':'-1','k':'i'}
adjDict['k'] = {'1':'k','i':'j','j':'-i','k':'-1'}

def calc(s,c):
    count = 0
    if s[0] == '-':
        count += 1
        s = s[1]
    if c[0] == '-':
        count += 1
        c = c[1]

    if adjDict[s][c][0] == '-':
        count += 1
        ret = adjDict[s][c][1]
    else:
        ret = adjDict[s][c]

    sign = '' if count % 2== 0 else '-'

    return sign + ret

def calc_i(s,c):
    _s = s
    _c = c
    count = 0
    if s[0] == '-':
        count += 1
        s = s[1]
    if c[0] == '-':
        count += 1
        c = c[1]

    if adjDict[s][c][0] == '-':
        count += 1
        ret = adjDict[s][c][1]
    else:
        ret = adjDict[s][c]

    sign = '' if count % 2 == 0 else '-'

    if calc(_s,sign+ret) != _c:
        sign = '' if sign == '-' else '-'

    return sign + ret

T = int(input())
for case in range(T):
    L,X = map(int,input().split())
    ijk = list(input())*X
    dp = [0 for i in range(L*X)]

    dp[0] = ijk[0]
    for i in range(1,L*X):
        dp[i] = calc(dp[i-1],ijk[i])

    ans = 'NO'
    for i in range(0,L*X):
        if dp[i] == 'i':
            for j in range(i+1,L*X)[::-1]:
                if calc_i(dp[j],dp[L*X-1]) == 'k' or (j == L*X and dp[j] == 'k'):
                    if calc_i(dp[i],dp[j]) == 'j':
                        ans = 'YES'
                        break
            else:
                continue
            break
    print("Case #{0}: {1}".format(case+1,ans))


