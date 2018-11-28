for i in range(input()):
    n, k = map(int, raw_input().split())
    l = [0]*(n+1)
    s = [(n,0)]
    trash = []
    while k >= 1:
        t = s.pop(0)
        l[t[1]+(t[0]+1)/2] = 1
        s.append(((t[0] + 1) / 2, t[1] + t[0] / 2))
        s.append(((t[0] - 1) / 2, t[1]))
        k -= 1
        trash.append(t[1]+(t[0]+1)/2)
    lr = 0;ls = 0
    k = trash.pop()
    for j in range(k+1, n+1):
        if l[j] == 1:
            break
        lr += 1
    for j in range(k-1, 0, -1):
        if l[j] == 1:
            break
        ls += 1
    print max(ls,lr), min(ls,lr)