import fileinput

e = 0
remaining = 0
for line in fileinput.input():
    if fileinput.isfirstline():
        continue

    if not remaining:
        e += 1
        D, N = line.strip().split()
        D = int(D)
        N = int(N)
        remaining = N
        ns = []
    else:
        K, S = line.strip().split()
        K = int(K)
        S = int(S)
        ns.append((K, S))
        remaining -= 1

    if not remaining:
        result = 0
        t = max((D - k) / s for k, s in ns)
        result = D / t


        print("Case #{}: {}".format(e, result))
