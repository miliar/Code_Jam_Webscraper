
def check(n):
    if n<10:
        return n
    ans=str(n)
    size=len(ans)
    ans=""
    num=str(n)
    i=0
    while i<(size-1):
        t=0
        if num[i]<num[i+1]:
            ans+=num[i]
            if (i+1)==(size-1):
                ans=ans+num[i+1]
                return ans
            
        if num[i]>num[i+1]:
            ans=ans+str(int(num[i])-1)
            break
        
        if num[i]==num[i+1]:
            lst1=[]
            repeat=num[i]
            (lst1,t)=handle(repeat,num[i+1:])
            for k in range(len(lst1)):
                ans+=str(lst1[k])
            if (t==-1):
                break
        i=i+1+t
        
    while len(ans)!=size:
        ans+='9'
    return int(ans)


def handle(repeat,num):
    j=0
    lst=[]
    while repeat==num[j]:
        if num[j+1:]=="":
            for k in range(j+2):
                lst.append(int(repeat))
            return (lst,-1)
        else:
            j+=1
    if num[j]<repeat:
        lst.append(int(repeat)-1)
        return (lst,-1)
    if num[j]>repeat:
        for k in range(j+1):
            lst.append(int(repeat))
        if num[j+1:]=="":
            lst.append(int(num[j]))
    return (lst,j)

def main():
    total=raw_input()
    for count in range(int(total)):
        print "Case #"+str(count+1)+": "+str(check(int(raw_input())))


if __name__=="__main__":
    main()
        
