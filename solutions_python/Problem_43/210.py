# usr/bin python
#-*- coding:utf-8 -*-

xnum = []
for i,line in enumerate(open(r"D:\pgz\py\A-large.in")):
    if i == 0:
        n = int(line.strip())
    else:
        xnum.append(line.strip())

f = open(r"D:\pgz\py\output.txt","w")
for i in range(n):
    x = xnum[i]
    s = len(set(x))
    if s == 1:
        s = 2
    lis = [0] + range(2,s)
##    print lis
    dic,su = {},0
    for j,y in enumerate(x):
        if j == 0:
            su = 1 * pow(s,len(x) -1)
            dic[y] = 1
        else:
            if y in dic:
               su += dic[y] * pow(s,len(x) -j-1)
            else:
                dic[y] = lis.pop(0)
                su += dic[y] * pow(s,len(x) -j-1)
    f.write("Case #%(num)d: %(su)d\n"%{"num":i+1,"su":su})
f.close()
