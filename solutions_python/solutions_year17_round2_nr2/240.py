
def sol(Y, R, B, acc):
    while True:
        if Y == 0 and R == 0 and B == 0:
            return acc
        if Y < 0 or R < 0 or B < 0:
            return []
        if acc[-1] == 'Y':
            if R >= B:
                acc.append('R')
                Y, R, B, acc = (Y, R-1, B, acc)
            else:
                acc.append('B')
                Y, R, B, acc = (Y, R, B-1, acc)
        elif acc[-1] == 'R':
            if Y >= B:
                acc.append('Y')
                Y, R, B, acc = (Y-1, R, B, acc)
            else:
                acc.append('B')
                Y, R, B, acc = (Y, R, B-1, acc)
        elif acc[-1] == 'B':
            if Y >= R:
                acc.append('Y')
                Y, R, B, acc = (Y-1, R, B, acc)
            else:
                acc.append('R')
                Y, R, B, acc = (Y, R-1, B, acc)





def solve():
    N, R, O, Y, G, B, V = map(int, raw_input().split())

    s = sol(Y-1, R, B, ['Y'])
    if s != [] and s[0] != s[-1]:
        return ''.join(s)
    s = sol(Y, R-1, B, ['R'])
    if s != [] and s[0] != s[-1]:
        return ''.join(s)
    s = sol(Y, R, B-1, ['B'])
    if s != [] and s[0] != s[-1]:
        return ''.join(s)
    return 'IMPOSSIBLE'
    

T = int(raw_input())
for t in range(1, T+1):

    print "Case #{}: {}".format(t, solve())
