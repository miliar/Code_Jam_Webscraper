# -*- coding: utf-8 -*-
# @Author: Pandarison
# @Date:   2017-04-08
# @Last Modified time: 2017-04-08

T = int(input())
for case_id in range(1, T+1):
    S,K = input().split()
    S = list(S)
    K = int(K)
    ans = 0
    for i in range(len(S)-K+1):
        if S[i] == '-':
            ans += 1
            for j in range(K):
                S[i+j] = '+' if S[i+j] == '-' else '-'
    #print("".join(S))
    if S.count('-') > 0:
        ans = "IMPOSSIBLE"
    print("Case #%d: %s"%(case_id, str(ans)))
