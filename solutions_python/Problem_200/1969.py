def check(n):
    s=[]
    flag=0
    while(n>0):
        s.append(n%10)
        n/=10
    s.reverse()
    for i in range(0,len(s)-1):
        if s[i]>s[i+1]:
            s[i]-=1
            if i!=0:
                if(s[i]<s[i-1]):
                    flag=1
            for j in range(i+1,len(s)):
                s[j]=9
            break
    r=0
    s.reverse()
    for i in range(0,len(s)):
        r = s[i]*pow(10,i) + r
    if flag==1:
        return check(r)
    return r

def main():
    t = input()
    l=0
    while l<t:
        n=input()
        print "Case #%d: %d"%(l+1,check(n))
        l+=1

if __name__ == '__main__':
    main()