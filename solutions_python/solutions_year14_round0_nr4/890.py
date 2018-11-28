import sys
import bisect

def play_war(nomis, kens):
    n = len(nomis)
    kens = list(kens)
    w = 0
    for i in xrange(n):
        j = bisect.bisect_left(kens, nomis[i])
        if j < len(kens):
            w += 1
            del kens[j]
        else:
            del kens[0]
    return n - w

def play_d_war(nomis, kens):
    n = len(nomis)
    nomis = list(nomis)
    kens = list(kens)
    y = 0

    while nomis:
        if nomis[0] < kens[0]:
            del nomis[0]
            del kens[len(kens)-1]
        else:
            del nomis[0]
            del kens[0]
            y += 1

    return y

f = open(sys.argv[1], 'r')

line = f.readline()
line = f.readline()

case = 1
while line:
    n = int(line) # num blocks
    nomis = [float(x) for x in f.readline().split()]
    kens = [float(x) for x in f.readline().split()]

    kens.sort()
    nomis.sort()

    z = play_war(nomis, kens)
    y = play_d_war(nomis, kens)

    print 'Case #%d: %d %d' % (case, y, z)

    line = f.readline()
    case += 1