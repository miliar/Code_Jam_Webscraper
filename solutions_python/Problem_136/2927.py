__author__ = 'Musunurus'

import math

file=open("B-large.in",'r')
file2=open("output.txt",'w')
t=int(file.readline())
d=[]
for i in range(t):


    k=file.readline().split()
    for p in range(3):

        k[p]=float(k[p])
    d.append(k)
file.close()

for i in range(t):
    c=d[i][0]
    f=d[i][1]
    x=d[i][2]

    best1=x/2
    best2=best1
    rate=2
    time=0
    while not (best1<best2):
        best1=best2
        irate=rate
        rate=rate+f
        time=time+(c/irate)
        best2=x/rate+time
    val=math.ceil(best1 * 10000000) / 10000000.0
    if val.is_integer():
        file2.write("Case #"+str(i+1)+": "+str(val)+"000000\n")
    else:
        file2.write("Case #"+str(i+1)+": "+str(val)+"\n")
file2.close()
