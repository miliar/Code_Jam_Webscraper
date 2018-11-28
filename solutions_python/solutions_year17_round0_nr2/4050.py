f1=open("op1.in","w")
with open("B-large.in") as f:
    testcase=f.readline().rstrip()
    t=0
    for line in f:
        t=t+1
        n1=line.strip()
        n=list()
        for i in n1:
            n.append(i)
        i=1
        l=len(n)
        if l==1:
            ans=n
        else:
            while(i<l):
                #print("i:",n[i],"i-1",n[i-1])
                if int(n[i])>=int(n[i-1]):
                    i=i+1
                else:
                    j=i-1
                    if int(n[j])-1<=int(n[j-1]):
                        while int(n[j])<=int(n[j-1]) and j>0:
                            j=j-1
                    n[j]=str(int(n[j])-1)
                    for j in range(j+1,len(n)):
                        n[j]='9'
        ans=''.join(n)
        if ans[0]=='0':
            ans=ans[1::]
        f1.write("Case #"+str(t)+": "+str(ans)+"\n")
f1.close()
f.close()
            
        
    
