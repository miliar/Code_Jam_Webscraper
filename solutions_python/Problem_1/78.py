#!/usr/bin/python

data = open('input.txt','rt').read().splitlines()
N = int(data[0])
k = 1

res = ""

for i in xrange(N):
    M = int(data[k])
    k+=1
    E = data[k:k+M]
    k+=M
    M1 = int (data[k])
    k+=1
    Q = data[k:k+M1]
    k+=M1
    temp = E
    count = 0 
    for j in Q:
        temp = [x for x in temp if x!=j];
        if len(temp)==0:
            temp = [x for x in E if x!=j]
            count +=1
    res+="Case #%d: %d\n" % (i+1,count)

open('output.txt','wt').write(res)

