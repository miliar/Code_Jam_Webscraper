t = int(input())
for i in range(1, t + 1):
    n, k = map(int, input().split())
    d = {n: 1}
    a = [n]
    num = n
    while len(a) >= 1:
        num = (sorted(a))[::-1][0]
        if num == 0:
            break
        if num % 2 == 0:
            x = num // 2
            y = x - 1
        else:
            x, y = num // 2, num // 2
        if x not in d.keys():
            if x != 0:
                d[x] = d[num]
                a.append(x)
        else:
            d[x] += d[num]
        if y not in d.keys():
            if y != 0:
                d[y] = d[num]
                a.append(y)
        else:
            d[x] += d[num]
        a.remove(num)
    for j in reversed(sorted(d.keys())):
        if k <= d[j]:
            ans = j
            break
        else:
            k -= d[j]
    if ans % 2 == 0:
        x = ans // 2
        y = x - 1
    else:
        x, y = ans // 2, ans // 2
    print("Case #{}: {} {}".format(i, x, y))
