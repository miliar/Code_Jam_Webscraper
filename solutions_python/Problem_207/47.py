def solve(t):
    N, R, O, Y, G, B, V = map(int, raw_input().split())
    ans = ''
    for i in xrange(N):
        if ans == '':
            if R >= Y and R >= B:
                R -= 1
                ans += 'R'
            elif Y >= R and Y >= B:
                Y -= 1
                ans += 'Y'
            else:
                B -= 1
                ans += 'B'
        elif ans[-1] == 'R':
            if Y == 0 and B == 0:
                ans = False
                break
            elif Y == B and ans[0] == 'Y':
                Y -= 1
                ans += 'Y'
            elif Y == B and ans[0] == 'B':
                B -= 1
                ans += 'B'
            elif Y >= B:
                Y -= 1
                ans += 'Y'
            else:
                B -= 1
                ans += 'B'
        elif ans[-1] == 'Y':
            if R == 0 and B == 0:
                ans = False
                break
            elif R == B and ans[0] == 'R':
                R -= 1
                ans += 'R'
            elif R == B and ans[0] == 'B':
                B -= 1
                ans += 'B'
            elif R >= B:
                R -= 1
                ans += 'R'
            else:
                B -= 1
                ans += 'B'
        else:
            if R == 0 and Y == 0:
                ans = False
                break
            elif R == Y and ans[0] == 'R':
                R -= 1
                ans += 'R'
            elif R == Y and ans[0] == 'Y':
                Y -= 1
                ans += 'Y'
            elif R >= Y:
                R -= 1
                ans += 'R'
            else:
                Y -= 1
                ans += 'Y'

    if ans is False or ans[0] == ans[-1]:
        ans = 'IMPOSSIBLE'
    print "Case #%d: %s" % (t, ans)

T = int(raw_input())
for t in xrange(1, T+1):
    solve(t)
