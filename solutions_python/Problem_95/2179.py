dic = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', 'q': 'z'}
f = open('A-small-attempt0.in', 'r')
times = int(f.readline())
saidas = []
for i in range(times):
    entrada = f.readline()
    saida = '' 
    for letra in entrada:
        if letra != '\n':
            saida += dic[letra]
    saidas.append(saida)

f1 = open('output', 'w')
for i in range(len(saidas)):
    f1.write('Case #%d: %s\n' % (i + 1, saidas[i]))
    print 'Case #%d: %s' % (i + 1, saidas[i])

