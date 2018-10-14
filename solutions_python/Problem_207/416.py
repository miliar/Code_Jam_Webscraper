def mane(inp):
    N, R, O, Y, G, B, V = map(int, inp.split(' '))
    R_ALL = R + O + V
    B_ALL = B + G + V
    Y_ALL = Y + O + G
    ls = [R, O, Y, G, B, V]
    h = N / 2
    if R_ALL > h or Y_ALL > h or B_ALL > h:
        return 'IMPOSSIBLE'
    seq = [-1] * N
    uni = ['R', 'O', 'Y', 'G', 'B', 'V']
    cur = ls.index(max(ls))
    pos = 0
    while -1 in seq:
        if ls[cur] > 0:
            ls[cur] -= 1
            seq[pos] = uni[cur]
            pos += 2
        else:
            cur = ls.index(max(ls))
        if pos >= N:
            if -1 in seq:
                pos = seq.index(-1)
    return ''.join(seq)


for i in range(int(input().strip())):
    print("Case #%d: %s" % (i + 1, mane(input().strip())))
