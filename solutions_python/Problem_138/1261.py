import sys

f = open(sys.argv[1])

ncases = int(f.readline())

def ken_select_stick(nao_stick, kens):
    index = -1
    minimum = 2

    for i in xrange(len(kens)):
        if (kens[i]>nao_stick):
            minimum = kens[i]
            index = i
            break

    if index == -1:
        return kens[0], kens[1:]

    return minimum, kens[0:index] + kens[index+1:]


def nao_select_stick(naos):
    return naos[0], naos[1:]


def nao_decei_select(naos, kens):
    min_ken = min(kens)
    if naos[0] < min_ken:
        index = -1
        for i in xrange(len(naos)):
            if (naos[i] > min_ken):
                index = i
                break
        if index == -1:
            return naos[0], naos[1:]

        return 1.0, naos[0:index] + naos[index+1:]

    return 1.0, naos[1:]


for i in xrange(ncases):
    n = int(f.readline())
    naos = map(float, f.readline().split())
    kens = map(float, f.readline().split())
    naos.sort()
    kens.sort()

#    print naos
#    print kens

    naos_new = naos
    kens_new = kens

    nao_score = 0
    ken_score = 0

    # Normal play
    for rnd in xrange(n):
        nao_stick, naos = nao_select_stick(naos)
        ken_stick, kens = ken_select_stick(nao_stick, kens)
        if (ken_stick > nao_stick):
            ken_score += 1
        elif (nao_stick > ken_stick):
            nao_score += 1

    nao_deci_score = 0
    ken_deci_score = 0
    for rnd in xrange(n):
        nao_stick, naos_new = nao_decei_select(naos_new, kens_new)
        ken_stick, kens_new = ken_select_stick(nao_stick, kens_new)
        if (ken_stick > nao_stick):
            ken_deci_score += 1
        elif (nao_stick > ken_stick):
            nao_deci_score += 1


    print "Case #%d: %d %d" % ((i+1), nao_deci_score, nao_score)
