def tidyn(n):
    if len(n) < 2:
        return int(n[0])

    b = False
    ans = int(''.join(n))
    while True:
        b = False
        for j in range(len(n)-1):
            if n[j] > n[j+1]:
                b = True
                continue
            if b:
                n[j] = '0'
        if b:
            n[len(n)-1] = '0'

        if not b:
            break

        ans = int(''.join(n)) - 1
        n = list(str(ans))

    return ans





t = int(input())
for i in range(1, t + 1):
    n = list(input())
    print("Case #{}: {}".format(i, tidyn(n)))

