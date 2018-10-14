import math, collections, copy, sys
f = open('input.in','r')
g = open('output.txt','w')
"""

"""
for index in xrange(1, int(f.readline()[:-1]) + 1):
    AC, AJ = [int(x) for x in f.readline()[:-1].split(' ')]
    C = [0]*AC
    J = [0]*AJ
    for i in xrange(AC):
        C[i] = [int(x) for x in f.readline()[:-1].split(' ')] + [0]
    for i in xrange(AJ):
        J[i] = [int(x) for x in f.readline()[:-1].split(' ')] + [1]
    D = sorted(C+J)
    C_extra = []
    J_extra = []
    switch = 0
    for i in xrange(AC+AJ-1):
        if D[i][2] != D[i+1][2]:
            switch += 1
        elif D[i][2] == 0 and D[i+1][2] == 0:
            C_extra.append(D[i+1][0]-D[i][1])
        else:
            J_extra.append(D[i+1][0]-D[i][1])
    if AC + AJ > 1:
        if D[-1][2] != D[0][2]:
            switch += 1
        elif D[-1][2] == 0 and D[0][2] == 0:
            C_extra.append(1440-D[i+1][1]+D[0][0])
        else:
            J_extra.append(1440-D[i+1][1]+D[0][0])
    TC = sum(C_extra)+sum(c[1]-c[0] for c in C)
    TJ = sum(J_extra)+sum(j[1]-j[0] for j in J)
    if TC <= 720 and TJ <= 720:
        result = str(max(2, switch))
    elif TC > 720:
        extra = TC - 720
        C_extra.sort(reverse = True)
        count = 0
        for t in C_extra:
            extra -= t
            count += 2
            if extra <= 0:
                break
        result = str(switch + count)
    elif TJ > 720:
        extra = TJ - 720
        J_extra.sort(reverse = True)
        count = 0
        for t in J_extra:
            extra -= t
            count += 2
            if extra <= 0:
                break
        result = str(switch + count)
    g.write("Case #{}: {}\n".format(index, result))
    print "Case #{}: {}\n".format(index, result)
f.close()
g.close()



# small case
#    if AC <= 1 and AJ <= 1:
#        result = str(2)
#    else:
#        if AC == 2:
#            D = C
#        else:
#            D = J
#        D.sort()
#        if D[1][1] - D[0][0] > 720 and D[1][0] - D[0][1] < 720:
#            result = str(4)
#        else:
#            result = str(2)