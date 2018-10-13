re = RealField(50)
re = RealField(40)
def find_first_ans(prb):
    fa = 41
    if prb > 1:
        return -1
    for i in range(0,40):
        cp = 1/(2^i)
        if prb >= 1/(2^i):
            if fa > i:
                fa = i
            prb -= cp
            if prb == 0:
                break

    if prb != 0 or fa > 40:
        fa = -1

    return fa

N = input()
for i in range(1,N+1):
    P = QQ(raw_input())
    res = find_first_ans(P)
    print "Case #%i: %s"%(i,res == -1 and "impossible" or str(res))
