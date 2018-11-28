t = int(input())
for test in range(t):
    smax, data = input().split()
    smax = int(smax)

    invited = 0
    standing = int(data[0])
    for i in range(1, smax+1):
        shy = int(data[i])
        if i > standing:
            invited += i - standing
            standing += i - standing
        standing += shy
    print("Case #{}: {}".format(test+1, invited))
