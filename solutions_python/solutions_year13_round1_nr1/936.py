import sys
def paint_needed(n, r):
    a_1 = 2*r+4*0+1;
    a_n = 2*r+4*(n-1)+1;
    res = (n*(a_1+a_n))/2;
    return res
def solve(r, t):
    lo = 0
    hi = 1<<64
    for it in range(64):
        mid = (lo+hi)>>1;
        if paint_needed(mid, r) > t:
            hi = mid-1
        else:
            lo = mid
    if paint_needed(hi, r) > t:
        print(lo)
    else:
        print(hi)

T = int(sys.stdin.readline())
for case in range(1, T+1):
    r, t = map(int, sys.stdin.readline().split())
    sys.stdout.write("Case #%d: "%case)
    solve(r, t)
