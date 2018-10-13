#!/usr/bin/python

data = open('B-small-attempt0.in','rt').read().splitlines()
N = int(data[0])
k = 1

res = ""

for i in xrange(N):
    tab = []
    T = int(data[k])
    k+=1
    NA,NB = map(int,data[k].split(' '))
    k+=1
    for j in xrange(NA):
        A,B = data[k].split(' ')
        k+=1
        A = map(int,A.split(':'))
        B = map(int,B.split(':'))
        A = A[0]*60+A[1]
        B = B[0]*60+B[1]
        tab.append((A,2,1))
        tab.append((B+T,1,2))

    for j in xrange(NB):
        B,A = data[k].split(' ')
        k+=1
        A = map(int,A.split(':'))
        B = map(int,B.split(':'))
        A = A[0]*60+A[1]
        B = B[0]*60+B[1]
        tab.append((A+T,1,1))
        tab.append((B,2,2))


    tab.sort()
    count=[0,0]
    r=[0,0]


    for j in tab:
        if j[1]==1:
            count[j[2]-1]+=1
        else:
            if count[j[2]-1]:
                count[j[2]-1]-=1
            else:
                r[j[2]-1]+=1
    res+="Case #%d: %d %d\n" % (i+1,r[0],r[1])

open('B-small-attempt0.out','wt').write(res)


