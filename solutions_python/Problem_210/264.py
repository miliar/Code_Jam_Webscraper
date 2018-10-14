
def parenting_partnering():
    A_C, A_J = map(int, raw_input().strip().split())
    C, J = [0] * A_C, [0] * A_J
    for i in xrange(A_C):
        C[i] = map(int, raw_input().strip().split())
    for i in xrange(A_J):
        J[i] = map(int, raw_input().strip().split())

    if A_C == 2:
        if C[0][0] > C[1][0]:
            C[0], C[1], = C[1], C[0]
        if C[1][1] - C[0][0] <= 720 or \
           1440 + C[0][1] - C[1][0] <= 720:
            return 2
        return 4
    if A_J == 2:
        if J[0][0] > J[1][0]:
            J[0], J[1], = J[1], J[0]
        if J[1][1] - J[0][0] <= 720 or \
           1440 + J[0][1] - J[1][0] <= 720:
            return 2
        return 4
    
        if max(K[0], K[1]) - min(J[0], J[1]) <= 720 or \
            min(J[0], C[1]) + 1400 - max(D[0], D[1]) <= 720:
            return 2
        return 4
    return 2

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, parenting_partnering())