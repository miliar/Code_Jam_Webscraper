def solve():
    c,f,x=map(float, raw_input().split())

    t=float(2)
    time=float(0)
    if x<c:
        return x/t

    while (x/(t+f) < (x-c)/t):
        time+=c/t
        t+=f

    time+=x/t
    return time


for i in range(int(raw_input().strip())):
    ans = solve()
    print "Case #%d: %.7f" % (i+1, float(ans))
