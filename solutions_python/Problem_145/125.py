from fractions import gcd

def solve(p,k):
    g = gcd(p,k)
    p = p/g
    k = k/g
    
    i = 0
    while 2** i < k:
        i += 1
        
    if 2** i != k:
        return "impossible"

    x = 1
    for j in range(i-1, -1, -1):
        if p >= 2**j:
            return str(x)
        x += 1


if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        p,k = map(int, raw_input().split("/"))
        print "Case #%d: %s" % (i, solve(p,k))

    

