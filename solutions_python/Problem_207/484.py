t = int(input())

for k in range(1, t+1):
    n, r, o, y, g, b, v = map(int, input().split())

    r = [r, "R"]
    y = [y, "Y"]
    b = [b, "B"]

    mi = min(filter(lambda x: x[0], [r, y, b]))

    e = [mi[1]]

    if mi[1] == "R":
        r[0] -= 1
    elif mi[1] == "Y":
        y[0] -= 1
    else:
        b[0] -= 1

    r[0] *= -1
    y[0] *= -1
    b[0] *= -1

    while r[0] or y[0] or b[0]:


        f = sorted(filter(lambda x: x[0] < 0 and x[1] != e[-1], [r, y, b]), key=lambda x: (x[0], x[1] != e[0]))

        if not f:
            e.append(e[-1])
            break

        ma = f[0]

        e.append(ma[1])

        if ma[1] == "B":
            b[0] += 1

        if ma[1] == "Y":
            y[0] += 1

        if ma[1] == "R":
            r[0] += 1

    for m, _ in enumerate(e):
        if e[m] == e[m-1]:
            e = "IMPOSSIBLE"
            #print(k)
            break


    print("Case #{}: {}".format(k, "".join(e)))
