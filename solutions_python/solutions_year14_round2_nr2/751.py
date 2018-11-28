'''
Created on May 3, 2014

@author: iiitbadmin
'''
g=open("two2.in","r")
h=open("out1.txt","w")
n=int(g.readline())
for i in range(n):
    line=g.readline().split()
    a=int(line[0])
    b=int(line[1])
    k=int(line[2])
    temp_a, temp_b=[],[]
    temp_k=[]
    for t in range(a):
        for j in range(b):
            temp_k.append(t&j)
    count=0
    for t in temp_k:
        if (t<k):
            count+=1
    string="Case #"+str(i+1)+": "+str(count)+"\n"               
    h.write(string)
h.close()
g.close()

            