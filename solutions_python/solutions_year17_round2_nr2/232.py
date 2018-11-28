def solve():
    N,R,O,Y,G,B,V = [int(v) for v in input().split()]
    l = [[R,'R'],[Y,'Y'],[B,'B']]
    l = sorted(l)
    if 2*l[-1][0] > sum(a[0] for a in l):
        return 'IMPOSSIBLE'
    ans = []
    while sum(a[0] for a in l) > 2:
        if len(ans) > 0 and ans[-1]==l[-1][1]:
            if l[-2][0]==0:
                return 'IMPOSSIBLE'
            ans.append(l[-2][1])
            l[-2][0] -= 1
            l = sorted(l)
        else:
            ans.append(l[-1][1])
            l[-1][0] -= 1
            l = sorted(l)
    if l[-1][0] == 2:
        return 'IMPOSSIBLE'
    if l[-1][1] == ans[0]:
        ans.append(l[-1][1])
        ans.append(l[-2][1])
    else:
        ans.append(l[-2][1])
        ans.append(l[-1][1])
    if ans[-1]==ans[0]:
        return 'IMPOSSIBLE'
    return ''.join(ch for ch in ans)

T = int(input())
for t in range(1, T + 1):
    print('Case #%d:' % t, solve())


