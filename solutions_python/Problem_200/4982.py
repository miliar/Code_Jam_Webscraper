last=0
t=""
flag=0
s=[]
f=open("B-small-attempt1.in",'r')
a=f.readline()
a.replace("\n","")
n=int(a)
sol= open("sol.txt",'w')

for i in range(0,n):
    a=f.readline()
    a.replace("\n","")
    l=int(a)
    for j in range(1,int(l)+1):
        s=[]
        last=0
        for x in str(j):
            s=s+[int(x)]        
        s.sort()
        for k in s:
           last=last*10+int(k)
        if(last==j):
           flag=(last)
    if(flag!=0):
       t=("Case #"+str(i+1)+": "+str(flag))
       sol.write(str(t))
       sol.write("\n")
sol.close()
