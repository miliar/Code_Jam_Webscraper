def flip(b, K, cakes, nb_hf):
    for i in range(b, b+K):
        if cakes[i] == '+':
            cakes[i] = '-'
            nb_hf -= 1
        else:
            cakes[i] = '+'
            nb_hf += 1

    return nb_hf

def isProblemDone(nb_hf, cakes):
    return nb_hf == len(cakes)

def getNbHf(cakes):
    nb_hf = 0
    for c in cakes:
        nb_hf += (c == '+')

    return nb_hf

def computeCakes(K, cakes):
    nb_hf = getNbHf(cakes)
    rounds = 0

    for i in range(len(cakes) - K + 1):
        if cakes[i] == '-':
            nb_hf = flip(i, K, cakes, nb_hf)
            rounds += 1

    if isProblemDone(nb_hf, cakes):
        return rounds
    else:
        return -1

t = int(raw_input())
for i in xrange(1, t + 1):
    uin = raw_input().split(" ")
    cakes = list(uin[0])
    K = int(uin[1])

    res = computeCakes(K, cakes)
    if res != -1:
        print("Case #" + str(i) + ": " + str(res))
    else:
        print("Case #" + str(i) + ": IMPOSSIBLE")
