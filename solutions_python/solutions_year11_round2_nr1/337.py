#!/usr/bin/python
#gcj 2011 roundA pa
T = int(input())
for cases in range(T):
    
    n = input()

    table=[]
    for i in range(n):
        table += [raw_input()]

    WP = {}
    for i in range(n):
        WP[i] = 0.0
        t=0
        for j in range(n):
            if table[i][j] == '1':
                WP[i] +=1
                t+=1
            elif table[i][j] =='0':
                t+=1
        WP[i]/=t

    OWP = {}
    for i in range(n):
        WP2 = {}
        for j in range(n):
            WP2[j]=0.0
            t=0
            for k in range(n):
                if k!=i:
                    if table[j][k]=='1':
                        WP2[j]+=1
                        t+=1
                    elif table[j][k]=='0':
                        t+=1 
            if t==0:
                WP2[j]=0
            else:
                WP2[j]/=t

        OWP[i] = 0.0
        t=0
        for j in range(n):
            if j!=i and table[i][j]!='.':
                OWP[i]+=WP2[j]
                t+=1
        OWP[i]/=t

    OOWP = {}
    for i in range(n):
        OOWP[i] = 0.0
        t=0
        for j in range(n):
            if j!=i and table[i][j]!='.':
                OOWP[i]+=OWP[j]
                t+=1
        OOWP[i]/=(t)

    print 'Case #' + str(cases+1)+':'

    for i in range(n):
        RPI = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]
        print RPI

