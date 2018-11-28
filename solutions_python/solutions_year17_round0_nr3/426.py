t=int(input())
for i in range(1,t+1):
    n,k = map(long,raw_input().split(' '))
    temp = k
    for b in range(70):
        # print temp
        if temp!=0:
            temp=temp>>1
        else:
            break
    b-=1
    b = 1<<b
    a = k-b
    s = (n-a)/b
    y,z = s/2,(s-1)/2
    # print (a,b,s)
    print("Case #{}: {} {}".format(i, y, z))