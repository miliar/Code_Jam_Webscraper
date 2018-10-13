t=(int)(input())
i=0

while(i<t):
    n=(int)(input())
    digits=[int(x) for x in str(n)]
    j=len(digits)-1
    
    while(j>=0):
        k=0
        f=1
        while(k<j):
            if(digits[j]<=digits[k]):
                f=0
                break
            k+=1
        if(f):
            f=0
            k=j+1
            while(k<len(digits)):
                if(digits[j]>digits[k]):
                    f=1
                    break
                k+=1
        if(f):
            break
        j-=1
    
    j+=1
    flg=0
    if(j!=0):
        while(j<len(digits)):
            digits[j]=0
            flg=1
            j+=1

    ans=int(''.join(str(i) for i in digits))
    if(flg):
        ans-=1
        
    print("Case #"+str(i+1)+":",ans)
    i+=1
