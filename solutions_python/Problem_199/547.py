def answer(row, k):
    flips = 0
    for i in range(len(row) - k + 1):
        is_sad = not row[i]
        if is_sad:
            flips += 1
            for j in range(i, i + k):
                row[j] = not row[j]
    return flips if all(row) else 'IMPOSSIBLE'

n = input()
for i in range(1, n + 1):
    (row, k) = tuple(raw_input().split(' '))
    row = map(lambda x: x == '+', list(row))
    k = int(k)
    res = answer(row, k)
    print('Case #' + str(i) + ': ' + str(res))