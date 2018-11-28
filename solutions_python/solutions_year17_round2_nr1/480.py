def piece(inp):
    D, N = map(int, inp.split(' '))
    h = {}
    for i in range(N):
        K, S = map(float, input().strip().split(' '))
        h[K] = S
    pos = list(h.keys())
    pos.sort(reverse=True)
    time = []
    for i in pos:
        time.append((D - i) / h[i])
    return D / max(time)


for i in range(int(input().strip())):
    print("Case #%d: %.6f" % (i + 1, piece(input().strip())))
