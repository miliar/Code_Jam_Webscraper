def needed(n, r):
    return 2*r*n + 2*n**2-n

def solve(r,t):
    ub = 1
    while needed(ub, r) <= t:
        ub *= 2
    lb = ub/2
    while lb < ub-1:
        mid = (lb+ub)/2
        x = needed(mid, r)
        if x == t:
            return mid
        if x > t:
            ub = mid
        else:
            lb = mid        
    return lb
        

if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        r,t = map(int, raw_input().split())
        print "Case #%d: %d" % (i, solve(r,t))
