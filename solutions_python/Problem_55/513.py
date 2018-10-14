a = open('C-small.in')
cases = int(a.readline().strip())
for case in range(1, cases + 1):
    linha = map(int, a.readline().strip().split(' '))
    corridas, maximo, grupos = linha[0], linha[1], linha[2]
    grupos = map(int, a.readline().strip().split(' '))
    ganhos = 0
    for corrida in xrange(corridas):
        lotacao = 0
        gnc = []
        while 1:
            if len(grupos) >= 1 and lotacao + grupos[0] <= maximo:
                lotacao += grupos[0]
                gnc.append(grupos.pop(0))
                if lotacao == maximo:
                    break
            else:
                break
        ganhos += sum(gnc)
        grupos += gnc
    print 'Case #%d: %d' % (case, ganhos)
a.close()
