
T = int(input())


def tidy(num):
    for i, x in enumerate(num[:-1]):
        if x > num[i+1]:
            return False
    return True


def change(N, num, poz):
    if poz != len(num):
        num[poz] = (num[poz]+9) % 10
        for i in range(poz+1, len(num)):
            num[i] = 9

    NN = int(''.join(map(str, num)))

    if NN <= N and tidy(num):
        return NN
    else:
        return None


for t in range(T):
    n_raw = input()
    N = list(map(int, n_raw))
    Ni = int(n_raw)
    ns = []
    for i, x in enumerate(N+[9]):
        c = change(Ni, N[:], i)
        if c is not None:
            ns.append(c)

    print('Case #{0:d}: {1:d}'.format(t+1, max(ns)))
