from collections import defaultdict

tamanho, npalavras, ncasos = map(int, raw_input().split())

palavras = [raw_input() for _ in xrange(npalavras)]
p = defaultdict(list)
for palavra in palavras:
    for indx, letra in enumerate(palavra):
        p[(letra, indx)].append(palavra)

for caso in xrange(ncasos):
    input = raw_input()

    group = False
    indx = 0
    possiveis = set()
    novos_possiveis = []
    for c in input:
        if c in '(':
            group = True
            novos_possiveis = []
        elif c == ')':
            if indx == 0:
                possiveis.update(novos_possiveis)
            else:
                possiveis.intersection_update(novos_possiveis)
            group = False
            indx += 1
        elif group:
            novos = p[(c, indx)]
            novos_possiveis.extend(novos)
        else:
            novos = p[(c, indx)]
            if indx == 0:
                possiveis.update(novos)
            else:
                possiveis.intersection_update(novos)
            indx += 1

    print "Case #%d: %d" % (caso + 1, len(possiveis))
