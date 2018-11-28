#!/usr/bin/python
f = open("B-small-attempt0.in", "r")
testcase = int(f.readline())
for qq in range(testcase): #i is testcase
    ans1 = 0
    splitline = f.readline().split(' ')
    row1=splitline
    row1[2] = row1[2].rstrip('\n')
    a=int(row1[0])
    b=int(row1[1])
    k=int(row1[2])
    if a>b:
        testtime=a;
    else:
        testtime=b;
    for i in range(a):
        for j in range(b):
            if (i & j)<k:
                ans1+=1

    #print(bin((1 | 2)))
    print('Case #'+str(qq+1)+': '+str(ans1))
    del row1[0:len(row1)]
