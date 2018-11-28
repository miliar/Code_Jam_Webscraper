f = open('C-small-attempt1.in', 'r')
dados = []
vezes = int(f.readline())
for vez in range(vezes):
    x = [int(k) for k in f.readline().split()]
    dados.append(x)
resultados = []
for j in dados:
    x1 = j[0]
    x2 = j[1]
    resultado = []
    for k in range(x1, x2 + 1):
        n_digt = len(str(x2))
        if n_digt <= 1:
            break
        for n in range(n_digt):
            c = int(str(k)[-n:] + str(k)[:-n])
            if c < x2 and c >= x1 and c < k:
                if resultado.count((c, k)) < 1:
                    resultado.append((c, k))
    resultados.append(resultado)
f1 = open('output', 'w')
for k in range(len(resultados)):
    f1.write('Case #%d: %d\n' % (k + 1, len(resultados[k])))
