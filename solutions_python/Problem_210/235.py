import numpy as np
import math



#------------------------------------
# Read inputs
t = int(raw_input())
for i in xrange(1, t + 1):
    Ac,Aj = [int(s) for s in raw_input().split(" ")]
    TA = []
    tc = 0
    tj = 0
    for j in range(0,Ac):
        tp = [int(s) for s in raw_input().split(" ")]
        TA.append((tp[0],tp[1],0))
    for j in range(0,Aj):
        tp = [int(s) for s in raw_input().split(" ")]
        TA.append((tp[0],tp[1],1))

    TA = sorted(TA)

    for j,ti in enumerate(TA):
        if ti[2]==0:
            tc += ti[1]-ti[0]
        else:
            tj += ti[1]-ti[0]

    to_remove = []
    dtc = []
    dtj = []
    for j,ti in enumerate(TA):
        if ti[2]==TA[j-1][2] and ti[2]==0:
            if (ti[0]-TA[j-1][1]+1440)%1440 + tc <= 720:
                dtc.append(((ti[0]-TA[j-1][1]+1440)%1440, j))
        if ti[2]==TA[j-1][2] and ti[2]==1:
            if (ti[0]-TA[j-1][1]+1440)%1440 + tj <= 720:
                dtj.append(((ti[0]-TA[j-1][1]+1440)%1440, j))

    # print dtc
    # print dtj

    yc = Ac + 0
    yj = Aj + 0

    to_remove = []
    for j in range(len(dtc)):
        if tc+dtc[j][0]<=720:
            yc -= 1
            tc += dtc[j][0]
            to_remove.append(dtc[j][1])

    for j in range(len(dtj)):
        if tj+dtj[j][0]<=720:
            yj -= 1
            tj += dtj[j][0]
            to_remove.append(dtj[j][1])

    # print yc, yj
    # print tc, tj
    # print to_remove


    print "Case #{}: {}".format(i, 2*max(yc,yj))
    # print
