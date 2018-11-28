#!/bin/python

TT = int(input())

for nt in range(1,TT+1):

    ans1 = int(input())
    m1 = [[int(i) for i in input().split() ] for j in range(4)]

    ans2 = int(input())
    m2 = [set([int(i) for i in input().split() ]) for j in range(4)]

    number = -1
    c = 0

    for i in m1[ans1-1]:
        if( i in m2[ans2-1] ):
            c += 1
            number = i

    if(c > 1):
        print("Case #%d: Bad magician!"%nt)
    elif(c == 1):
        print("Case #%d: %d"%(nt,number))
    else:
        print("Case #%d: Volunteer cheated!"%(nt))
