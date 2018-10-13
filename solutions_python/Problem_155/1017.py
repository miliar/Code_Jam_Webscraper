T = int(raw_input())

def can_clap(audience):
    clappers = 0
    for i in range(len(audience)):
        if clappers >= i:
            clappers += audience[i]
    return clappers == sum(audience)

for case in range(T):
    Smax, S = raw_input().split()
    Smax = int(Smax)
    S = map(int, S)
    added_clappers = 0
    while not can_clap(S):
        added_clappers += 1
        S[0] += 1

    print "Case #{}: {}".format(case + 1, added_clappers)
