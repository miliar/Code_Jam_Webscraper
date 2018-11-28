
import sys

ntests = int(sys.stdin.readline())

for ncase in range(ntests):
    Nd = [int(d) for d in sys.stdin.readline().strip()]

    while True:
        firstDrop = None
        for i in range(len(Nd) - 1):
            if Nd[i] > Nd[i + 1]:
                firstDrop = i
                break
        else:
            break

        for i in range(firstDrop + 1, len(Nd)):
            Nd[i] = 9

        Nd[firstDrop] -= 1

        if firstDrop == 0 and Nd[firstDrop] == 0:
            Nd = Nd[1:]

    print('Case #{0}: {1}'.format(ncase + 1, ''.join([str(d) for d in Nd])))
