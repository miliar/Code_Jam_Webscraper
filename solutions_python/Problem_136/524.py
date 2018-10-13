fp = open('B-large.in')
out = open('B-large.txt','w')
T = int(fp.readline())
casno = 1
while T!=0:
    T-=1
    C,F,X = map(float,fp.readline().split())
    OUT = X/2.0
    D = 2.0
    S = 0
    while True:
        S += 1.0/D
        D += F
        TT = C * S + X / D
        if TT<OUT:
            OUT = TT
        else:
            break
    print OUT
    out.write('Case #%d: ' % casno)
    out.write('%.8f\n' % OUT)
    casno +=1 
