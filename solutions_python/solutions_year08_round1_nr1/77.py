#!/usr/bin/python
n = input();
for i in range(n):
    k = input();
    l1=[];
    l2=[];
    s1 = raw_input().split(' ')
    s2 = raw_input().split(' ')
    for j in range(k):
        l1.append(int(s1[j]))
    for j in range(k):
        l2.append(int(s2[j]))

    l1.sort();
    l2.sort();
    tot=0;
    for j in range(k):
        tot+=l1[j]*l2[k-j-1]
    print "Case #"+str(i+1)+":",tot

