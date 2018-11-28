def answer(sps, k):
    spas = dict()
    for s in sorted(sps, reverse=True):
        k -= sps[s]
        if k <= 0:
            return (spaces(s)[0], spaces(s)[1])
        spas[spaces(s)[0]] = spas.get(spaces(s)[0], 0) + sps[s]
        spas[spaces(s)[1]] = spas.get(spaces(s)[1], 0) + sps[s]
    # return (spas, k)
    return answer(spas, k)

def spaces(n):
    if n == 1:
        return (0, 0)
    if n == 2:
        return (1, 0)
    if n == 3:
        return (1, 1)
    if n % 2 == 0:
        return (int(n / 2), int(n / 2 - 1))
    return (int((n - 1) / 2), int((n - 1) / 2))

t = int(input())
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(' ')]
    print('Case #{}: {} {}'.format(i, answer({n: 1}, k)[0], answer({n: 1}, k)[1]))
