from sys import stdin
buf = []
for line in stdin:
    buf.insert(0, [int(e) for e in line.strip().split()])

Q = 100

P = [0 for i in range(Q+1)]
for ii in range(Q+1):
    i = ii
    j = Q
    for f in [2, 2, 5, 5]:
        if not (i % f or j % f):
            i /= f
            j /= f
    P[ii] = j
# print P

def solve(l):
    ''' exists D in (0..N] such that (
D*pD/100 in [0..D) and exists G in [N....) such that (
G*pG/100 in [0..G) ) ).
generaly, with enough large G pG doesn't matter.
 '''
    N, pD, pG = l[0], l[1], l[2]
    if not (pG % 100):
        return pD == pG
    return (P[pD] <= N)

T = buf.pop()[0]
for i in range(1, T+1):
    ans = solve(buf.pop())
    print 'Case #' + str(i) + ': ' + ['Broken', 'Possible'][ans]
