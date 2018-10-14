for i in range(int(input())):
    l=input().split()
    n=int(l[1])
    s=list(l[0])
    ans=0
    while(True):
        if '-' in s:
            ind=s.index('-')
            if(ind+n>len(s)):
                print("Case #"+str(i+1)+": IMPOSSIBLE")
                break
            for j in range(n):
                if(s[ind+j]=='-'):
                    s[ind+j]='+'
                else:
                    s[ind+j]='-'
            ans+=1
        else :
            print("Case #"+str(i+1)+":",ans)
            break
