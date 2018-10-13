T = int(input())

for t in range(1,T+1):
    N = int(input())

    s = list(map(int,str(N)))
    
    f = True
    while f:
        f = False
        for i in range(1, len(s)):
            if not f and s[i] < s[i-1]:
                s[i-1] -= 1
                f = True
            if f: s[i] = 9

    N = ''
    for i in s:
        if i: N += str(i)
    
    print("Case #{}: {}".format(t,N))