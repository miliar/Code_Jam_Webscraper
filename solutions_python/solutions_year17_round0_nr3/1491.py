def get_empty(n, k):
    if k == 1:
        if n % 2:
            ret = (n-1)//2
            return ret, ret
        else:
            ret = n//2
            return ret, ret - 1
    else:
        kn = k//2

        if k % 2 and not n % 2:
            nn = n//2 -1        
        else:
            nn = n//2

        return get_empty(nn, kn)


t = int(input())
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    y, z = get_empty(n, k)
    print("Case #{}: {} {}".format(i, y, z)) 



