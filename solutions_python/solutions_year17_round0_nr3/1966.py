import math
import itertools

def l(stalls, start):
    current = start - 1

    while current >= 0:
        if stalls[current] == 1:
            return start - current
        current -= 1

    return 0

def r(stalls, start):
    current = start + 1

    while current < len(stalls):
        if stalls[current] == 1:
            return current - start
        current += 1

    return 0

def printstalls(stalls, *a):
    print(''.join('.' if i == 0 else '#' for i in stalls), *a)

def f(n, k):
    stalls = [0] * (n + 2)
    stalls[0] = 1
    stalls[n + 1] = 1

    Z = []

    for p in range(1, k+1):
        data = []
        for i in range(1, len(stalls) - 1):
            if stalls[i] == 1:
                continue

            ls = l(stalls, i)
            rs = r(stalls, i)
            n = min(ls, rs)
            x = max(ls, rs)
            data.append([n, x, i])


        result = sorted(data, reverse=True)[0]
        n, x, i = result
        stalls[i] = 1

        # g = math.log(p) / math.log(2)
        # g = int(g) + 1
        # g = 2 ** g
        # nn = int((len(stalls) - 2 - p) / g)
        # assert nn == n - 1

        # xx = int((len(stalls) - p) / g)
        # assert (xx == x - 1) or (xx + 1 == x - 1)

        # if xx + 1 == x - 1:
        #     Z.append(((xx, x - 1), p))

    # for (a, b), z in itertools.groupby(Z, key=lambda x: x[0]):
    #     z = [i[1] for i in z]
    #     print(a, b, min(z), max(z), len(z))

    return "%d %d" % (x - 1, n - 1)

def main():
    N = int(input())
    for t in range(1, N + 1):
        n, k = input().split()
        n, k = int(n), int(k)
        print("Case #%d: %s" % (t, f(n, k)))

main()
