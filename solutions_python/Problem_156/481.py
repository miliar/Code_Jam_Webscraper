C={}
def m(P):
    if P[0]<=3:
        return P[0]
    if P not in C:
        C[P] = 1 + m(tuple(p-1 for p in P if p>1))
        for q in range(1, P[0]):
            C[P] = min(C[P], 1 + m(tuple(sorted(P[1:]+(P[0] - q, q), reverse=True))))
    return C[P]
for t in range(input()):
    _=input()
    P=tuple(sorted(map(int,raw_input().split()), reverse=True))
    print 'Case #%d: %r'%(t+1,m(P))