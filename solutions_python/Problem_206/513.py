for _ in range(int(input())):
    d,n = list(map(int, input().split()))
    time = 0
    for __ in range(n):
        k,s = list(map(int, input().split()))
        t = ((d-k)/s)
        if t > time:
            time = t
    s = d/time
    s = round(s,6)
    print("Case #"+str(_+1)+": "+str(s))
