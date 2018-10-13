t = int(input())
for i in range(t):
    batp = list()
    n,k=input().split(" ")
    n,k = [int(n),int(k)]
    stack = [0]*2
    p = n//2
    stack[0]=p
    stack[1]=(n-p-1)
    batp.append(stack[0])
    batp.append(stack[1])
    for j in range(k-1):
        q = max(batp)
        #print(q)
        for h in range(len(batp)-1):
            if q==batp[h]:
                del batp[h]
                break
        stack[0] = q//2
        batp.append(stack[0])
        if q-(q//2)-1>0:
            stack[1] = q-(q//2)-1
            batp.append(stack[1])
        else:
            stack[1]=0
            batp.append(stack[1])
        #print(batp)
    batp.pop()
    print("Case #{}: {} {}".format(i+1,max(stack),min(stack)))
