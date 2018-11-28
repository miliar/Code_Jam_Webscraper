t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    r = [n]
    for j in range(k):
        l = r.pop(0) - 1
        s = (l)//2
        if s == (l)/2:
            b = s
        else:
            b = s + 1
        if b in r:
            w = r.index(b)
            r = r[:w] + [b] + r[w:]
        else:
            r.append(b)
        r.append(s)
    print("Case #{}: {} {}".format(i, b, s))