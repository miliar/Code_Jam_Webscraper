T = int(raw_input())

for case in range(T):
    S, values = raw_input().split()
    values = map(int, values)

    total = 0
    need = 0
    for i, v in enumerate(values):
        if total < i:
            total += i - total
        total += v

    print "Case #{}: {}".format(case + 1, total - sum(values))