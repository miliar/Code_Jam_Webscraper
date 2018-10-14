T = int(input())


def compute(n, k):

    #print("\t {}  {}".format(n,k))

    if n == 0:
        return (0,0)
    if k == 1:
        if n % 2 == 1:
            return ( (n-1)/2 , (n-1)/2 )
        else:
            return ( n/2 -1 , n/2 )
            
    
    nOdd = (n % 2 == 1)
    kOdd = (k % 2 == 1)
    
    if nOdd and kOdd:
        return compute( (n-1)/2 , (k-1)/2)
    elif nOdd and not kOdd:
        return compute( (n-1)/2 , (k)//2)
    elif not nOdd and kOdd:
        return compute( n/2 - 1, (k-1)/2)
    elif not nOdd and not kOdd:
        return compute( n/2, k / 2)
        


for t in range(T):
    n, k = map(int, input().split())
    ans_max, ans_min = map(int, compute(n , k))
    print("Case #{}: {} {}".format(t+1, ans_min, ans_max))
    
    