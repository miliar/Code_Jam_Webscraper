f=open("B.in", 'r')
g=open("B_sol.txt", 'w')
T=int(f.readline().strip())
for i in range(T):
    ans=''
    now=f.readline().strip()
    length=len(now)
    strongly_increase=[]
    first_decrease=-1
    for j in range(length-1):
        if(int(now[j])<int(now[j+1])):
            strongly_increase.append(j)
        elif(int(now[j])>int(now[j+1])):
            first_decrease=j
            break
    if(first_decrease==-1):
        ans=now
    else:
        if(strongly_increase==[]):
            if(now[0]=='1'):
                ans='9'*(length-1)
            else:
                ans=str(int(now[0])-1)+'9'*(length-1)
        else:
            strongly_increase.reverse()
            k=strongly_increase[0]
            ans=now[:k+1]+str(int(now[k+1])-1)+'9'*(length-k-2)
    g.write("Case #%d: %s\n"%(i+1, ans))
f.close()
g.close()
                
                    
            