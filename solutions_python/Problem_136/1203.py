def detN(X, F, C):
    N = (round(((X*F-2*C)/(F*C)-0.5)))
    if N < 0:
        return 0
    else:
        return N
def detT(X, F, C):
    N = detN(X,F,C)
    T = X/(2+((N)*F))
    for i in range(0, int(N)):
        T = T + C/(2+i*F)
    return T
T = int(raw_input())
B = open('GCJ2k14A2.out','w')
for i in range(1,T+1):
    C, F, X = raw_input().split()
    C, F, X = float(C), float(F), float(X)
    B.write("Case #" + str(i) + ": " + str(detT(X,F,C)) + "\n")
B.close()
