
import sys
stin = sys.stdin

T = int(stin.readline())

for icase in range(T):
    line = stin.readline()
    tokens = line.split()
    N = int(tokens[0])
    PD = int(tokens[1])
    PG = int(tokens[2])

    broken = False
    if 0 != PD and 0 == PG:
        broken = True
    elif 100 != PD and 100 == PG:
        broken = True
    else:
        f2 = 2
        f5 = 2
        rem = PD
        if rem % 2 == 0:
            f2 -= 1
            rem /= 2
        if rem % 2 == 0:
            f2 -= 1
            rem /= 2
        if rem % 5 == 0:
            f5 -= 1
            rem /= 5
        if rem % 5 == 0:
            f5 -= 1
            rem /= 5

        min_need = 1
        for i in range(f2):
            min_need *= 2
        for i in range(f5):
            min_need *= 5

        if not (min_need <= N):
            broken = True

    reply = "Possible"
    if broken:
        reply = "Broken"

    print "Case #%d:" % (icase+1), reply
