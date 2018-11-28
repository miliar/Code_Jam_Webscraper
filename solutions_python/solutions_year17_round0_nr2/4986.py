fh=open("B-small-attempt1.in","r")
fw=open("B-small.txt","w")
T=int(fh.readline())
count=0
str1=''
for j in range(T):
    n=int(fh.readline())
    #n=int(input())
    flag=False
    #print("uybuy")
    while(flag==False):
        s=str(n)
        L2=[]
        chk=int(s[0])
        m=0
        for i in range(1,len(s)):
            if(int(s[i])>=chk):
                chk=int(s[i])
            else:
                m=1
                break
        if(m==0):
            #print(n)
            #print(j)
            str1+="Case #"+str(j+1)+": "+str(n)+'\n';
            flag=True
            continue
        n-=1
str1.strip()
fw.write(str1)
fw.close()
fh.close()
            
        
        
