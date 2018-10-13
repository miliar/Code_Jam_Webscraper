#!/usr/bin/env python


f1 = file('a-in.txt')

t = int(f1.readline())

for k in range(1, t+1):
    x = int(f1.readline())
    for i in range(1,5):
        tt = f1.readline()
        if x ==i:
            xx = tt.split()
    y = int(f1.readline())
    for i in range(1,5):
        tt = f1.readline()
        if y ==i:
            yy = tt.split()
    ret = 0
    flag = 0
    for j in xx:
        for jj in yy:
            if j == jj:
                ret = int(j)
                flag = flag + 1
    if flag ==1:
        print 'Case #'+ str(k)+': '+str(ret)
    elif flag==0:
        print 'Case #'+ str(k)+': Volunteer cheated!'
    elif flag>1:
        print 'Case #'+ str(k)+': Bad magician!' 
                
    