def vira_panquecas(posicao, panquecas, tamanho):
    panquecas_viradas = ""
    for i in range(posicao):
        panquecas_viradas += panquecas[i]

    for i in range(tamanho):
        panqueca = panquecas[i+posicao]
        if panqueca == "+":
            panquecas_viradas += "-"
        if panqueca == "-":
            panquecas_viradas += "+"

    for i in range(posicao + tamanho, len(panquecas)):
        panquecas_viradas += panquecas[i]

    return panquecas_viradas


testes = int(raw_input())
for i in range(testes):
    ent = raw_input()

    separa = ent.split()
    S = separa[0]
    K = int(separa[1])

    j = 0
    tentativas = 0
    while j < (len(S) - K + 1):
        y = ""
        for k in range(K):
            y += S[j+k]
        if y.startswith("-"):
            S = vira_panquecas(j, S, K)
            tentativas += 1
        j += 1

    if "-" in S:
        print "Case #%d: IMPOSSIBLE" % (i+1)
    else:
        print "Case #%d: %d" % (i+1, tentativas)
