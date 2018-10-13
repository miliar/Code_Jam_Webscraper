
def solve():
    t=int(input())
    for i in range(1,t+1):
        s,c=input().split()
        l=len(s)
        c=int(c)
        if all('+'== k for k in s):
            print("Case #{}: 0".format(i))
        elif all('-'==k for k in s):
            if l%c==0:
                print("Case #{}: {}".format(i,l//c))
            else:
                print("Case #{}: IMPOSSIBLE".format(i))
        else:
            l1=[True if k=='+' else False for k in s]
            res=0
            for j in range(len(l1)-c+1):
                if l1[j]==0:
                    res+=1
                    for k in range(c):
                        l1[j+k]=not l1[j+k]
            if any(k==False for k in l1):
                print("Case #{}: IMPOSSIBLE".format(i))
            else:
                print("Case #{}: {}".format(i,res))
                
                
solve()












