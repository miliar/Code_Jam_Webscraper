
T = input()

for t in range(T):
    N = input()
    ds = []
    ls = []
    for n in range(N):
        d, l = map(int, raw_input().split())
        ds.append(d)
        ls.append(l)
    D = input()

    reached = [0] * N
    reached[0] = ds[0]

    ok = False
    for i in range(N):
        length = reached[i]
        if D - ds[i] <= length:
            ok = True
            break
        if length == 0:
            continue

        for j in range(i+1, N):
            if ds[j] - ds[i] <= length:
                to_height = min(ds[j]-ds[i], ls[j])
                if to_height > reached[j]:
                    reached[j] = to_height



    print 'Case #%d: %s' % (t+1, ok and 'YES' or 'NO')
