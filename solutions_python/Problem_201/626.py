T = int(input().strip())

def getans( seps , k ):
    L = min(seps)
    R = max(seps)
    while k > 0:
        a = sorted(seps.keys())[::-1]
        for key in a:
            L = (key - 1)//2
            R = key - L - 1
            if not L in seps: seps[L] = 0
            if not R in seps: seps[R] = 0
            seps[L] += seps[key]
            seps[R] += seps[key]
            if k <= seps[key]:
                return R,L
            k -= seps[key]
            del(seps[key])
    return R,L


for i in range(T):
    n, k = input().strip().split()
    n, k = int(n),int(k)
    tmp = k
    seps = {n: 1}
    lg = 0
    y,z = getans(seps,k)
    print( "Case #{}: {} {}".format(i+1,y,z))
