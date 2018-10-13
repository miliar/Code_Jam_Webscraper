def odd(lower,upper, k):
    mid = (upper+lower)/2
    k = k/2
    if k == 1:
        mini = (mid-lower) if (mid-lower)<(upper-mid) else(upper-mid)
        maxi = (mid-lower) if (mid-lower)>(upper-mid) else(upper-mid)
        return mini,maxi
    else:
        if k%2 == 0:
            return odd(mid+1, upper, k)
        else:
            return odd(lower, mid-1, k)

def even(lower, upper, k):
    mid = (upper+lower)/2
    k = k/2
    if k == 1:
        mini = (mid-lower) if (mid-lower)<(upper-mid) else(upper-mid)
        maxi = (mid-lower) if (mid-lower)>(upper-mid) else(upper-mid)
        return mini,maxi
    else:
        if k%2 == 0:
            return even(mid+1, upper, k)
        else:
            return even(lower, mid-1, k)

def number(n, k):
    mini = 0; maxi = 0;
    if n%2 == 1:
        if k ==1:
            mini = n/2
            maxi = n/2
        elif k%2 == 0:
            mini,maxi = odd(1,n/2, k)
        else:
            mini,maxi = odd(((n+1)/2)+1, n, k)
    else:
        if k == 1:
            mini = n/2-1
            maxi = n/2
        elif k%2 == 0:
            mini,maxi = even(n/2+1, n, k)
        else:
            mini,maxi = even(1,n/2-1, k)
    print(str(maxi)+" "+str(mini))

if __name__ == "__main__":
    t = int(input())
    for i in range(1,t+1):
        n,k = raw_input().split()
        n = int(n)
        k = int(k)
        print "Case #%d:" %(i),
        number(n,k)
