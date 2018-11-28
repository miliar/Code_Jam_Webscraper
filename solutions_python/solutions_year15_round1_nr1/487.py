def first_method(M):
    eat = 0
    for i in range(1, len(M)):
        eat += max(M[i - 1] - M[i], 0)

    return eat


def second_method(M):
    rate = max(max(0, M[i - 1] - M[i]) for i in range(1, len(M)))
    return sum(min(rate, M[i - 1]) for i in range(1, len(M)))


T = int(input())

for t in range(1, T + 1):
    N = int(input())

    M = [int(i) for i in input().split()]

    y = first_method(M)
    z = second_method(M)

    print("Case #{}: {} {}".format(t, y, z))
