from sys import stdin


def is_tidy(n):
    k = 9
    while n > 0:
        tmp = n % 10
        if tmp <= k:
            k = tmp
            n //= 10
            continue
        else:
            return False

    return True


T = int(stdin.readline().rstrip())

for i in range(1, T + 1):
    N = int(stdin.readline().rstrip())
    for j in reversed(range(1, N + 1)):
        if is_tidy(j):
            print("Case #{0}: {1}".format(i, j))
            break
