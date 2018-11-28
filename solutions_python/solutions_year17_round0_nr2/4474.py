#!/usr/bin/python
fo = open("B-large.in", "r+")
f=open("output.txt","w")

t=int(fo.readline())
for i in range(t):
    n=int(fo.readline())
    st=str(n)
    l=len(st)
    for j in range(l-1):
        if(int(st[l-j-1])<int(st[l-j-2])):
            if(j!=0):
                st=st[:l-j-1]+'9'+st[l-j:]
            else:
                st=st[:l-j-1]+'9'
            if(j!=0):
                if(st[l-j]<st[l-j-1]):
                    st=st[:l-j]+''.join('9' for k in range(j))        
            st=st[:l-j-2]+str(int(st[l-j-2])-1)+st[l-j-1:]
    count=0
    for j in range(l):
        if(st[j]!='0'):
            break
        else:
            count+=1
    st=st[count:]            
    f.write("case #"+str(i+1)+": "+st)
    f.write("\n")

fo.close()
f.close()