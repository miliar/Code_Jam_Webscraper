def func(n,s):
    cur=0
    req=0
    for j in range(n+1):
        a=int(s[j])
       # print(a)
        if(j<=cur):
            cur=cur+a            
        else:
            req=req+(j-cur)
            cur=cur+a+(j-cur)
    return req

import re
file=open("A-large.in","r")
d=file.read()
file.close()
fw=open("output.txt","w")
p=re.findall("\d+",d);
t=int(p[0])
count=1

for i in range((t)):
    n=int(p[count])
    count=count+1
    s=p[count]
    #print(n)
    #print(s)
    count=count+1
    val=str(func(n,s))
    #print(val)
    #print("Case #",(i+1),": ",val,sep="",end="\n")
    fw.write("Case #")
    s=str((i+1))
    fw.write(s)
    fw.write(": ")
    val=val+""
    fw.write(val)
    fw.write("\n")
    
fw.close()
    


