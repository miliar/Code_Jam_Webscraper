import math

t = int(input() )
for i in range(t):
    n,k = map(int,input().split() )
    pan = []
    for j in range(n):
        pan.append( list(map(int,input().split() ) ) )
        pan[j].append( 2*math.pi*pan[j][0]*pan[j][1] )
        temp = pan[j][0]
        pan[j][0] = pan[j][2]
        pan[j][2] = temp

    pan.sort()
    #print(pan)
    big =0
    ans =0.0
    for j in range(k-1):
        ans+=pan[n-k+1+j][0]
        big = max(big,pan[n-k+1+j][2])

    extra =0
    for j in range(n-k+1):
        bignow =0
        bignow = max(big,pan[j][2])
        extra = max(extra, pan[j][0] +math.pi*bignow*bignow)

    print("Case #"+str(i+1)+": "+str(ans+extra) )
                       

    
