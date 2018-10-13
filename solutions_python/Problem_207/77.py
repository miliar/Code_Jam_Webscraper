# -*- coding: utf-8 -*-
import sys
IMPOSSIBLE = "IMPOSSIBLE"

T = int(raw_input())
for case in xrange(1, T + 1):
    N, R, O, Y, G, B, V = map(int, raw_input().split()) 
    mx = max(R, Y, B)
    if 2*mx > N:
        ans = IMPOSSIBLE
    else:
        ans = [""]*N
        if R == mx:
            for i in xrange(0, N, 2):
                if R: ans[i] = "R"; R -= 1
                elif Y: ans[i] = "Y"; Y -= 1
                elif B: ans[i] = "B"; B -= 1
            for i in xrange(1, N, 2):
                if Y: ans[i] = "Y"; Y -= 1
                elif B: ans[i] = "B"; B -= 1
                elif R: ans[i] = "R"; R -= 1
        elif Y == mx: 
            for i in xrange(0, N, 2):
                if Y: ans[i] = "Y"; Y -= 1
                elif R: ans[i] = "R"; R -= 1
                elif B: ans[i] = "B"; B -= 1
            for i in xrange(1, N, 2):
                if R: ans[i] = "R"; R -= 1
                elif B: ans[i] = "B"; B -= 1
                elif Y: ans[i] = "Y"; Y -= 1
        else:
            for i in xrange(0, N, 2):
                if B: ans[i] = "B"; B -= 1
                elif R: ans[i] = "R"; R -= 1
                elif Y: ans[i] = "Y"; Y -= 1
            for i in xrange(1, N, 2):
                if R: ans[i] = "R"; R -= 1
                elif Y: ans[i] = "Y"; Y -= 1
                elif B: ans[i] = "B"; B -= 1
        for i in xrange(N):
            assert ans[i] != ans[(i + 1)%N]
        ans = "".join(ans)
    print "Case #%d: %s" % (case, ans)

