t = int(input())
for x in range(t):
    n = int(input())
    nl = [str(i) for i in range(1, n + 1)][::-1]
    tidy = 0
    for i in nl:
        if int(i) < 10:
            tidy = int(i)
            break
        else:
            c = int(i[:1])
            for j in i:
                if int(j) < c:
                    break
                else:
                    c = int(j)
            else:
                tidy = int(i)
        if tidy != 0:
            break
    print('Case #{}: {}'.format(x + 1, tidy))
