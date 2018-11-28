T = int(input())

for i in range(T):
    n = list(map(int, input()))
    prev = 0
    prev_idx = 0
    asc = True
    for idx, j in enumerate(n):
        if j > prev:
            prev = j
            prev_idx = idx
            continue
        elif prev == j:
            continue
        else:
            asc = False
            break

    if not asc:
        if prev == 1:
            n = [9 for i in range(len(n)-1)]
        else:
            n[prev_idx] = prev-1
            for ind, j in enumerate(n[prev_idx+1:]):
                n[prev_idx+1 + ind] = 9

    n = (list(map(str, n)))
    n = ''.join(n)
    n = int(n)
    print('Case #' + str(i+1) + ': ' + str(n))
