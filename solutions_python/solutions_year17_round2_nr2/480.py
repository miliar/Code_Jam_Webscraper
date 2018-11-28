t = int(input())
for i in range(t):
    n, r, o, y, g, b, v = map(int, input().split())
    if r + o + v > n // 2 or o + g + y > n // 2 or g + b + v > n // 2:
        print('Case #%d: IMPOSSIBLE' % (i + 1))
        continue
    if o > b or v > y or g > r:
        print('Case #%d: IMPOSSIBLE' % (i + 1))
        continue
    if b > r + o + y or r > b + g + y or y > b + v + r:
        print('Case #%d: IMPOSSIBLE' % (i + 1))
        continue

    res = []
    while o > 0:
        o -= 1
        b -= 1
        res.append("O")
        res.append("B")
    while v > 0:
        v -= 1
        y -= 1
        res.append("V")
        res.append("Y")
    while g > 0:
        g -= 1
        r -= 1
        res.append("G")
        res.append("R")

    ls = [r, b, y]
    ch = ["R", "B", "Y"]
    p = 0

    leftover = ""
    if len(res) > 0 and len(res) < n:
        if res[0] == "O":
            leftover = "B"
            ls[1] -= 1
        elif res[0] == "G":
            leftover = "R"
            ls[0] -= 1
        elif res[0] == "V":
            leftover = "Y"
            ls[2] -= 1

    last_idx = -1
    while ls[0] > 0 or ls[1] > 0 or ls[2] > 0:
        mx = max(ls)
        idx = ls.index(mx)
        if idx == last_idx:
            mx = ls[(idx + 1) % 3]
            idx = (idx + 1) % 3
            if ls[(idx + 2) % 3] > mx:
                mx = ls[(idx + 1) % 3]
                idx = (idx + 1) % 3
        ls[idx] -= 1
        res.append(ch[idx])
        last_idx = idx

    if leftover != "":
        res.append(leftover)
    if res[0] == res[-1]:
        res[-1], res[-2] = res[-2], res[-1]
    print('Case #%d: %s' % (i + 1, ''.join(res)))
