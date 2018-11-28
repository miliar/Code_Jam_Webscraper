# -*- coding: shift_jis -*-
# matching features of two images
import sys
import numpy as np



original=0
a = []
check = []
beautiful = []


for l in open('B-small-attempt2.in').readlines():
    data = l[:-1].split(' ')
    a += [int(data[0])]


T = a[0]
del a[0]


for i in range(T):
    for j in range(a[i]):
        check1=a[i]-j
        check2=check1
        num = []
        while check1 != 0:
            num.append(check1 % 10)
            check1 /= 10
        num.reverse()
        check = num[:]
        num.sort()
        if(num == check):
            beautiful.append(check2)
            break


fout = open("result.txt","w")
for k in range(T):
    fout.writelines("Case #%d: %d" % (k+1,beautiful[k]) + "\n")
