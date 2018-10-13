t = int(raw_input().strip())
for xyz in range(1, t+1):
    n, p = list(map(int, raw_input().strip().split()))
    ans = 0
    if p == 2:
        x = list(map(int, raw_input().strip().split()))
        o, e = [0, 0]
        for i in range(n):
            if x[i] % 2 == 0:
                e += 1
            else:
                o += 1
        ans = e+((o+1)/2)
    elif p == 3:
        x = list(map(int, raw_input().strip().split()))
        o, e, j = [0, 0, 0]
        for i in range(n):
            if x[i] % 3 == 0:
                e += 1
            elif x[i] % 3 == 1:
                o += 1
            else:
                j += 1
        ans = e+min(o, j)+((max(o, j)-min(o, j)+2)/3)
    else:
        x = list(map(int, raw_input().strip().split()))
        o, e, j, z = [0, 0, 0, 0]
        for i in range(n):
            if x[i] % 4 == 0:
                o += 1
            elif x[i] % 4 == 1:
                e += 1
            elif x[i] % 4 == 2:
                j += 1
            else:
                z += 1
        ans = o+min(e, z)+(j/2)+(max(e, z)-min(e, z)+3)/4
        if j % 2 == 1:
            if (max(e, z)-min(e, z)) % 4 == 0 or (max(e, z)-min(e, z)) % 4 == 3:
                ans += 1
    print("Case #"+str(xyz)+": "+str(ans))
