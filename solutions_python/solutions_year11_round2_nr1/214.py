import sys

T = int(sys.stdin.readline())

for _ in range(T):
    print "Case #%d: " % (_ + 1)
    teamNum = int(sys.stdin.readline())
    input = []
    for __ in range(teamNum):
        input.append(list(sys.stdin.readline().strip()))
    
    WP = []
    for i in range(teamNum):
        subTotal = []
        for j in range(teamNum):
            if input[i][j] != '.':
                subTotal.append(int(input [i][j]))
        if len(subTotal) != 0:
            WP.append(float(sum(subTotal))/len(subTotal))
        else:
            WP.append(0.0)
    OWP = []
    for i in range(teamNum):
        subTotal = []
        for j in range(teamNum):
            if j == i or input [j][i] == '.':
                continue
            _subTotal = []
            for k in range(teamNum):
                if input[j][k] != '.' and k != i:
                    _subTotal.append(int(input[j][k]))
            subTotal.append(float(sum(_subTotal))/len(_subTotal))
        OWP.append(float(sum(subTotal))/len(subTotal))
    OOWP = []
    for i in range(teamNum):
        subTotal = []
        for j in range(teamNum):
            if input[i][j] != '.':
                subTotal.append(OWP[j])
        if len(subTotal) != 0:
            OOWP.append(float(sum(subTotal))/len(subTotal))
        else:
            OOWP.append(0.0)

    for i in range(teamNum):
        print 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]
        
                





