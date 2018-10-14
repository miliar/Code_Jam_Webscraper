t = int(input())
for i in range(1, t + 1):
    num = int(input())
    for n in range(num, 0, -1):
        n = str(n)
        istidy = True
        if len(n) > 1:
            for dIndex in range(len(n) - 1, 0, -1):
                if int(n[dIndex]) < int(n[dIndex - 1]):
                    istidy = False
                    break
        if istidy:
            ans = n
            break
    print("Case #{}: {}" . format(i, ans))
