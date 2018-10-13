
find=[['0','1','i','j','k'],['1','1','i','j','k'],['i','i','-1','k','-j'],['j','j','-k','-1','i'],['k','k','j','-i','-1']]
def helper(a,b):
    n=0
    m=0

    if a[0]=='-':

        if a[1]=='1' :
            n=1
        elif a[1]=='i':
                n=2
        elif a[1]=='j':
            
                n=3
        else:
            n=4
        if b=='1' :
            m=1
        elif b=='i':
            
                m=2
        elif b=='j':
            
                m=3
        else:
            m=4
        temp=find[n][m]
        if temp[0]=='-':
            ans = temp[1]
        else :
            ans= '-'+temp
        
    else:
        if b=='1' :
            m=1
        elif b=='i':
            
                m=2
        elif b=='j':
            
                m=3
        else:
            m=4
        if a=='1' :
            n=1
        elif  a=='i':
           
                n=2
        elif a=='j':
            
                n=3
        else:
            n=4
        ans=find[n][m]

    return ans
t=int(input())
case_count=1
for i in range(t):
    lastpos=0;
    itrue=False
    jtrue=False
    ktrue=False
    temp=input().split()
    size=int(temp[0])
    x=int(temp[1])
    l=list(input())

    for i in range(size*(x-1)):
        l.append(l[i%size])
##    print(l)
    for i in range(size*x-1):
        lastpos=i
##        print(l[i])
        if l[i]=='i':
            itrue=True
            break
##        print("first:"+l[i]+",second:"+l[i+1])
        l[i+1]=helper(l[i],l[i+1])
##        print("result:"+l[i+1])
##        print("helper:",i,":",l[i+1])
        
    temp=lastpos
    for i in range(temp+1,size*x-1):
        lastpos=i
##        print(l[i])
        if l[i]=='j':
            jtrue=True
            break
##        print("first:"+l[i]+",second:"+l[i+1])
        l[i+1]=helper(l[i],l[i+1])
##        print("result:"+l[i+1])
##        print("helper:",i,":",l[i+1])
    temp=lastpos
    for i in range(temp+1,size*x-1):
##        print(l[i])
##        print("first:"+l[i]+",second:"+l[i+1])
        l[i+1]=helper(l[i],l[i+1])
##        print("result:"+l[i+1])
##        print("helper:",i,":",l[i+1])

    if l[size*x-1]=='k':
        ktrue=True
    elif l[size*x-1]=='j':
        jtrue=True
    elif l[size*x-1]=='i':
        itrue=True
##    print(itrue,jtrue,ktrue)
        
    if itrue==True and jtrue==True and ktrue==True:
        print ("Case #"+str(case_count)+": "+"YES")
    else:
        print ("Case #"+str(case_count)+": "+'NO')
        
    case_count+=1
        
