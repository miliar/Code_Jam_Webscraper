f=open("B-large.in")
lines=f.readlines()
l=[]
for i in lines[1:]:
    l.append(int(i.strip()))
#print(l)    

ans=[]
_c=0
for case in l:
    _c+=1
    if len(str(case))==1:
        print("Case #{:}: {:}".format(_c,case))
        continue
    l=list(str(case))
    l=[int(i) for i in l]
    leng=len(l)
    ans=0
    while True:
        for i in range(1,len(l)):
            if l[i]<l[i-1]:
            
                break
        #print(i,l)    
        if i==len(l)-1 and  l[i]>=l[i-1]:
            p=""
            for kk in l:
                p+=str(kk)
            ans=int(p)
            break
        else:
            #print(i,l)
            l[i-1]-=1
            l=l[:i]+[9]*(len(l)-i)
            if l[0]==0:
                l=l[1:]
                
    print("Case #{:}: {:}".format(_c,ans))                
    
