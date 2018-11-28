def tidy(n, c):
    while True:
        ans = n
        past = ans % 10
        fail = -1
        id = 0
        while (ans > 0):
            ans //= 10
            curr = ans % 10
            if curr > past or past == 0:
                fail = id
                break
            past = curr
            id += 1
        if fail != -1:
            n -= 10 ** id if id == 0 else 10 ** (id - 1)
            # print(id)
        else:
            break
    print("Case #{}: {}".format(c, n))


with open('large.in', 'r') as fin:
    T = int(fin.readline().strip())
    for i in range(1, T + 1):
        N = int(fin.readline().strip())
        tidy(N, i)
