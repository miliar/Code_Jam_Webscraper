import os

def check(s,N):
    if len(s) != N: return False
    if len(s) < 2: return True
    if s[0] == s[-1]: return False
    for i in xrange(len(s)-1):
        if s[i] == s[i+1]: return False
    return True

def triple(l,k):
    g = l[0][1]+l[1][1]+l[2][1]
    l[0][0] -= k
    l[1][0] -= k
    l[2][0] -= k
    return g*k


def solve(N, R, O, Y, G, B, V):
    l = [[Y,'Y'], [R, 'R'], [B, "B"]]
    l.sort(reverse=True)
    if l[0][0] > N/2:
        return 'IMPOSSIBLE'

    a,b,c = l[0][0], l[1][0], l[2][0]
    t1 = c - (a-b)
    res = triple(l,t1)
    c = ''
    g = []
    for i in xrange(N-3*t1):
        bb = False
        for j in xrange(3):
            if l[j][0] > 0 and c != l[j][1]:
                c = l[j][1]
                l[j][0] -= 1
                g.append(c)
                bb = True
                break
        if not bb: print 'AAAAAAAAAA'
    res += ''.join(g)
    if not check(res, N):
        res = res[1]+res[0]+res[2:]
    if not check(res, N):
        print 'GGGGGGGGGGGGG'
    return res


with open(os.path.expanduser("~/PycharmProjects/gcj/2017/1B/B.in")) as f:
    m = int(f.readline().strip('\n'))
    # print m
    for i in range(m):
        N, R, O, Y, G, B, V = [int(x) for x in f.readline().strip().split()]
        res = solve(N, R, O, Y, G, B, V)

        print 'Case #' + str(i+1) + ': ' + str(res)