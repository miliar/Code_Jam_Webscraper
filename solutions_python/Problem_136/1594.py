import sys

def deboCrearGranja(C, F, X, cps):
    tt = X / cps
    tg = C / cps
    tf = X / (cps + F)
    if tt < tg + tf:
        return 0
    else:
        return 1

entrada = open("B-large.in", 'r')
salida = open("salida.txt", 'w')

T = int(entrada.readline())
for caso in range(1, T + 1):
    t = tuple(map(float, entrada.readline().split(' ')))
    C = t[0]
    F = t[1]
    X = t[2]
    cps = 2.0
    nf = 0
    ts = 0.0
    while (C < X) and deboCrearGranja(C, F, X, cps):
        nf = nf + 1
        ts = ts + C / cps
        cps = cps + F
    ts = ts + X / cps
    salida.write("Case #%d: %s\n" % (caso, "%.7f" % ts))

salida.close()
entrada.close()