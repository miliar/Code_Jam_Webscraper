
def get_answer(D, N, KS):

    max_t = 0
    for i, k, s in KS:

        dt = (D - k) / s
        max_t = max(max_t, dt)

    return D / max_t

    ## sort by Ki
    #sKS = sorted(KS, key=lambda x: x[2])

    #pre_start = sKS[0][1]
    #pre_speed = sKS[0][2]
    #t = (D - pre_start) / pre_speed

    #for x in sKS[1:]:
    #
    #    if x[1] >= pre_start:
    #        continue
    #    t_meet = (x[1]-pre_start)/(pre_speed-x[2])
    #    t -




t = int(input())
for i in range(1, t + 1):
    D, N = input().split(' ')
    D, N = int(D), int(N)

    KS = []
    for j in range(N):
        k, s = input().split(' ')
        k, s = int(k), int(s)
        KS.append((j, k, s))

    answer = get_answer(D, N, KS)
    print("Case #{}: {}".format(i, answer))
