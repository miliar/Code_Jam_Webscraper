for i in range(int(input())):
    t, s = input().split()
    t = int(t)
    ov = int(s[0])
    inv = 0
    for c in range(1, t + 1):
        if c > ov:
            dif = c - ov
            inv += dif
            ov += dif
        ov += int(s[c])
    print("Case #" + str(i + 1) + ": " + str(inv))