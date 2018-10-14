
def solve(cipher):
    lst = range(1, int(cipher)+1)
    tidy = []
    for i in lst:
        if istidy(i)==True:
            tidy.append(i)
    return tidy[-1]


def istidy(n):
    l = map(int, str(n))
    return all(a <= b for a, b in zip(l[:-1], l[1:]))
