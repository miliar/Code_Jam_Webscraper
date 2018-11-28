import sys
from collections import defaultdict


def check(A, B, C):
    s = A + B + C
    if A > s // 2:
        return False
    if B > s // 2:
        return False
    if C > s // 2:
        return False
    x,y,z = sorted([[A, 'R'], [B, 'B'], [C, 'Y']], reverse=True)
    ans = [0]*s
    stri = x[0]*x[1] + y[0]*y[1] + z[0]*z[1]
    if s % 2 == 1:
        for i in range(s):
            ans[2*i % s] = stri[i]
    else:
        for i in range(s // 2):
            ans[2*i] = stri[i]
        for i in range(s // 2):
            ans[2*i+1] = stri[i + s // 2]
    return ans

def run(C):
    s, R, O, Y, G, B, V = C

    if s == R + G:
        if R != G:
            return False
        return ['R', 'G'] * R
    if s == O + B:
        if O != B:
            return False
        return ['O', 'B'] * O
    if s == V + Y:
        if V != Y:
            return False
        return ['V', 'Y'] * V


    if G >= R and G > 0:
        return False
    if O >= B and O > 0:
        return False
    if V >= Y and V > 0:
        return False

    start = check(R-G, B-O, Y-V)
    if not start:
        return False
    ans = []
    g = False
    o = False
    v = False
    for k in start:
        ans.append(k)
        if k == 'R' and not g:
            ans.extend(['G', 'R'] * G)
            g = True
        if k == 'B' and not o:
            ans.extend(['O', 'B'] * O)
            o = True
        if k == 'Y' and not v:
            ans.extend(['V', 'Y'] * V)
            v = True
    assert len(ans) == s
    nr = sum(1 for x in ans if x == 'R')
    nb = sum(1 for x in ans if x == 'B')
    ny = sum(1 for x in ans if x == 'Y')
    assert nr == R and nb == B and ny == Y
    return ans

f = file(sys.argv[1],'r')
T = int(f.readline().strip())
for case in range(1,T+1):
    C = [int(x) for x in f.readline().strip().split()]
    ans = run(C)
    if not ans:
        print 'Case #%d: IMPOSSIBLE' % (case,)
    else:
        print 'Case #%d: %s' % (case, ''.join(ans))
