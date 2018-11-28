import sys

filename = sys.argv[1]

f = open('%s.in' % filename)
g = open('%s.out' % filename, 'w')

DEBUG = sys.argv[2] if len(sys.argv) >= 3 else False
def dlog(s, *n):
    if DEBUG:
        if n:
            print(s % tuple(n))
        else:
            print(s)

def single(two, l2, one, l1, total):
    if two == one and two > 0 and two + one == total:
        return (l2 + l1) * (total / 2)
    if two == one - 1 and two > 0 and two + one == total:
        return 'IMPOSSIBLE'
    return False

def solve(N, R, O, Y, G, B, V):

    s = (single(G, 'G', R, 'R', N) or 
         single(O, 'O', B, 'B', N) or 
         single(V, 'V', Y, 'Y', N))
    if s:
        return s

    if (G >= R and G > 0) or (O >= B and O > 0) or (V >= Y and V > 0):
        return 'IMPOSSIBLE'

    R -= G
    B -= O
    Y -= V
    N = R + B + Y

    colors = [[R, 'R', 'RG' * G + 'R'],[B, 'B', 'BO' * O + 'B'],[Y, 'Y', 'YV' * V + 'Y']]

    if (R > N / 2 or B > N / 2 or Y > N / 2) and N > 1:
        dlog("%d %d %d %d", N, R, B, Y)
        return 'IMPOSSIBLE'

    ans = ''

    for _ in range(N):
        dlog(colors)
        colors.sort(reverse=True)
        if ans and colors[0][1] == ans[-1]:
            ibest = 1
        else:
            ibest = 0
        best = colors[ibest]

        if sum([x[0] for x in colors]) == 2:
            if ans and colors[1 - ibest][1] == ans[0]:
                ibest = 1 - ibest
                best = colors[ibest]

        best[0] -= 1
        if best[2]:
            ans += best[2]
            best[2] = None
        else:
            ans += best[1]

    return ans

T = int(f.readline())
for t in range(T):
    dlog("Case %d", t)
    line = f.readline().strip().split()

    N = int(line[0])
    R = int(line[1])
    O = int(line[2])
    Y = int(line[3])
    G = int(line[4])
    B = int(line[5])
    V = int(line[6])

    ans = solve(N, R, O, Y, G, B, V)

    g.write('Case #%d: %s' % (t + 1, ans))
    g.write('\n')


