import sys

entrada = open("D-large.in", 'r')
salida = open("salida.txt", 'w')

T = int(entrada.readline())
for caso in range(1, T + 1):
    N = int(entrada.readline())
    lN = list(map(float, entrada.readline().split(' ')))
    lK = list(map(float, entrada.readline().split(' ')))
    lN.sort()
    lK.sort()
    lN2 = list(lN)
    lK2 = list(lK)
    sW = 0
    sDW = 0

    for b in range (N - 1, -1, -1):
        if lN[0] > lK[b]:
            sW = sW + b + 1
            break
        elif lK[0] > lN[b]:
            break
        else:
            for c in range(0, b + 1):
                if lN[0] < lK[c]:
                    lN.pop(0)
                    lK.pop(c)
                    break

    for b in range (N - 1, -1, -1):
        if lN2[0] > lK2[b]:
            sDW = sDW + b + 1
            break
        elif lK2[0] > lN2[b]:
            break
        else:
            for c in range(b, -1, -1): # (0, b + 1):
                if lN2[b] > lK2[c]:
                    lN2.pop(b)
                    lK2.pop(c)
                    sDW = sDW + 1
                    break

    salida.write("Case #%d: %d %d\n" % (caso, sDW, sW))

salida.close()
entrada.close()