import math
a_0=int(input())
z=a_0
while a_0>0:
    a_0-=1
    n,kase=input().split()
    n,kase=[int(n),int(kase)]
    u=math.ceil(n/2)-1
    v=n-math.ceil(n/2)
    stack=[u,v]
    if kase==1:
        mn=max(stack[0],n-stack[0]-1)
        op=min(stack[0],n-stack[0]-1)
        print("Case #{}: {} {}".format(z-a_0,mn,op))
    else:
        for i in range(2,kase+1):
            x=max(stack)
            del stack[stack.index(max(stack))]
            u=math.ceil(x/2)-1
            v=x-math.ceil(x/2)
            stack.append(u)
            stack.append(v)
        mn=max(u,v)
        op=min(u,v)
        print("Case #{}: {} {}".format(z-a_0,mn,op))
        
