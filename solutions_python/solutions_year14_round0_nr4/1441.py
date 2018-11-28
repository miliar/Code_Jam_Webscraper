T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    naomi = sorted(map(float, input().split()))
    ken = sorted(map(float, input().split()))

    # deceit
    deceit = 0
    n = 0
    m = 0
    for i in range(N):
        if naomi[i] > ken[m]:
            deceit += 1
            m += 1

    # war
    war = 0
    for i in range(N):
        cur = naomi[i]
        for each in ken:
            if cur < each:
                ken.remove(each)
                break
        else:
            del ken[0]
            war += 1

    print("Case #{0}: {1} {2}".format(test_case, deceit, war))