for yu in range (int(input())):
    n=input()
    n=[i for i in n]
    l=len(n)
    for i in range (l-1,0,-1):
        if int(n[i])<int(n[i-1]):
            j=i
            n[i-1]=str(int(n[i-1])-1)
            while j<l:
                n[j]='9'
                j+=1
    t=''
    for i in n:
        if int(i)<0:
            1==1
        else:
            t+=i
    print('Case #'+str(yu+1)+':',int(t))

        
    
    
