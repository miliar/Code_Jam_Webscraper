import sys

def solve(c_haveto, j_haveto, c_opt, j_opt, both_can):
    additional = 0
    while c_haveto < 720-both_can and c_opt:
        if c_opt[0]>720+both_can-c_haveto:
            break
        c_haveto += c_opt.pop(0)
    while c_haveto < 720-both_can and j_opt:
        c_haveto += j_opt.pop()
        additional += 2
    return additional + len(c_opt)*2

for Pr in xrange(1, input()+1):
    Ac, Aj = [int(x) for x in raw_input().split()]
    C, D = [None]*Ac, [None]*Ac
    J, K = [None]*Aj, [None]*Aj
    if Ac==0 and Aj==0:
        print 'Case #%d: 0'%(Pr)
        continue
    for i in xrange(Ac):
        C[i], D[i] = [int(x) for x in raw_input().split()]
    for i in xrange(Aj):
        J[i], K[i] = [int(x) for x in raw_input().split()]
    C.sort()
    D.sort()
    J.sort()
    K.sort()
    c_haveto, j_haveto = 0, 0
    c_opt, j_opt = [], []
    both_can = 0
    last_c = True
    last_end = 0
    if Ac==0:
        last_c = False
        last_end = K[Aj-1]
    elif Aj==0:
        last_end = D[Ac-1]
    elif C[Ac-1] < K[Aj-1]:
        last_c = False
        last_end = K[Aj-1]
    else:
        last_end = D[Ac-1]

    last_end = last_end - 1440
    change = 0
    c, j = 0, 0
    C.append(sys.maxint)
    J.append(sys.maxint)
    for i in xrange(Ac+Aj):
        if C[c]<J[j]:
            c_haveto += D[c]-C[c]
            if last_c:
                c_opt.append(C[c]-last_end)
            else:
                both_can += C[c]-last_end
                change += 1
                last_c=True
            last_end = D[c]
            c+=1
        else:
            j_haveto += K[j]-J[j]
            if last_c:
                both_can += J[j]-last_end
                change += 1
                last_c=False
            else:
                j_opt.append(J[j]-last_end)
            last_end = K[j]
            j+=1
    c_opt.sort()
    j_opt.sort()
    while c_opt and c_opt[0] == 0:
        c_opt.remove(0)
    while j_opt and j_opt[0] == 0:
        j_opt.remove(0)
    R = min(solve(c_haveto, j_haveto, c_opt[:], j_opt[:], both_can),solve(j_haveto, c_haveto, j_opt[:], c_opt[:], both_can))
    print 'Case #%d: %d'%(Pr, change+R)