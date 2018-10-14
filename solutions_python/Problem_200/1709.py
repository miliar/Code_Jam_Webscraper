import sys
if len(sys.argv) > 1:
    entrada = open(sys.argv[1])
else:
    entrada = open('b.in')
N = int(entrada.readline())

vistos = dict()


def recursion(numero, cap):
    assert numero >= 0
    if cap == 0:
        return 0
    if numero < 10:
        return min(max(numero, 0), cap)
    if (numero, cap) in vistos:
        return vistos[(numero, cap)]

    alta = numero / 10
    baja = min(numero % 10, cap)

    op1 = recursion(alta, baja) * 10 + baja
    op2 = recursion(alta - 1, 9) * 10 + 9
    m = max(op1, op2)
    vistos[(numero, cap)] = m
    return m

for caso in xrange(1, N + 1):
    linea = entrada.readline().strip()
    T = int(linea)
    print 'Case #' + str(caso) + ':', recursion(T, 9)
