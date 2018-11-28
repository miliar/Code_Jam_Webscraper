import sys

entrada = open("A-small-attempt0.in", 'r')
salida = open("salida.txt", 'w')

T = int(entrada.readline())
for caso in range(1, T + 1):
    row = int(entrada.readline())
    for i in range(1, row):
        entrada.readline()
    r1 = tuple(map(int, entrada.readline().split(' ')))
    if row < 4:
        for i in range(row + 1, 5):
            entrada.readline()
    row = int(entrada.readline())
    for i in range(1, row):
        entrada.readline()
    r2 = tuple(map(int, entrada.readline().split(' ')))
    if row < 4:
        for i in range(row + 1, 5):
            entrada.readline()
    s = set(r1).intersection(r2)

    if len(s) == 1:
        salida.write("Case #%d: %d\n" % (caso, s.pop()))
    elif len(s) == 0:
        salida.write("Case #%d: Volunteer cheated!\n" % caso)
    else:
        salida.write("Case #%d: Bad magician!\n" % caso)
entrada.close()
salida.close()