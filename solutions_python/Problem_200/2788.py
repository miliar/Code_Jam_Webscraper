n = int(input())
for b in range(1, n+1):
    y = int(input())
    k = [int(x) for x in list(str(y))]
    for i in range(len(k)-1,0,-1):
        if(k[i-1] > k[i]):
            k[i-1]-=1
            for j in range(i, len(k)):
                k[j] = 9
    print("Case #{}: {}".format(b, int(''.join(str(v) for v in k))))