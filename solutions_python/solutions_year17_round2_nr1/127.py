def f(d,n):
    time_to_end = 0
    horses = []
    for line in range(n):
        k,s = map(int,input().split())
        time_to_end = max(time_to_end, (d - k)/s)
    return d / time_to_end

T = int(input())
for case in range(1, T+1):
    d,n = map(int, input().split())
    ans = f(d,n)
    print("Case #%s: %s" % (case, ans))

