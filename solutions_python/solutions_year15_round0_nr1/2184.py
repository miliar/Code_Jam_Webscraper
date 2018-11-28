for case in range(1, int(input()) + 1):
    s = [int(s) for s in input().split()[1]]
    clapping = 0
    for i, people in enumerate(s):
        if people > 0:
            clapping += max(i - clapping, 0)
            clapping += people
    print("Case #{}: {}".format(case, clapping - sum(s)))
