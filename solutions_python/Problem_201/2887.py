n = int(input())
for i in range(n):
    a, b = (int(s) for s in input().split())
    x = [0, a + 1]
    if a == b:
        print("Case #{}:".format(i + 1), 0, 0)
        continue
    for j in range(b):
        x.sort()
        mini = -1
        maxi = -1
        plek = 0
        for l in range(len(x) - 1):
            for k in range(x[l] + 1, x[l + 1]):
                s = k - int(x[l]) - 1
                r = int(x[l + 1]) - k - 1
                c = min(s, r)
                d = max(s, r)
                if c > mini:
                    mini = c
                    plek = k
                    maxi = d
                elif c == mini and d > maxi:
                    plek = k
                    maxi = d
        y = maxi
        z = mini
        x.append(plek)
    print("Case #{}:".format(i + 1), y, z)
