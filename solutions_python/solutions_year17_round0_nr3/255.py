def calc(N, S):
    np = 1
    n = 2
    while True:
        if S <= (n - 1):
            break
        np = n
        n *= 2
    empty = (N - np + 1)
    size = empty / np
    if S <= (np - 1 + empty % np):
        size += 1
    emptyS = size - 1
    S_min = emptyS / 2
    S_max = emptyS - S_min
    return S_max, S_min

with open('C-large.in') as inp:
    with open('output.txt', 'w') as outp:
        ncases = int(inp.readline().strip())
        for nc in range(0, ncases):
            [N, K] = inp.readline().strip().split(' ')
            S_max, S_min = calc(int(N), int(K))
            outp.write('Case #{}: {} {}\n'.format(nc + 1, S_max, S_min))