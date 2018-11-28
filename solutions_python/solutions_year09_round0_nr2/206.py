from sys import stdin, stdout

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def alphayield():
    for a in alpha:
        yield a

def base(mapa, inclinacion, i, j):
    menor = inclinacion[i][j]
    mejor_i = i
    mejor_j = j
    if mapa[i][j] != "":
        valor = mapa[i][j]
    else:
        if i > 0 and inclinacion[i-1][j] < menor:
            menor = inclinacion[i-1][j]
	    mejor_i = i-1
	    mejor_j = j
        if j > 0 and inclinacion[i][j-1] < menor:
	    menor = inclinacion[i][j-1]
	    mejor_i = i
	    mejor_j = j-1
        if j < len(inclinacion[i])-1 and inclinacion[i][j+1] < menor:
	    menor = inclinacion[i][j+1]
	    mejor_i = i
	    mejor_j = j+1
        if i < len(inclinacion)-1 and inclinacion[i+1][j] < menor:
            menor = inclinacion[i+1][j]
	    mejor_i = i+1
	    mejor_j = j
	if i == mejor_i and j == mejor_j:
	    valor = siguiente.next()
	else:
	    valor = base(mapa, inclinacion, mejor_i, mejor_j)
    mapa[i][j] = valor
    return valor
T = int(stdin.readline())

for i in range(0, T):
    siguiente = alphayield()
    partes = stdin.readline().split(' ')
    H = int(partes[0])
    W = int(partes[1])
    inclinacion = [ [0 for j in range(0, W)] for k in range(0, H)]
    mapa = [ ["" for j in range(0, W)] for k in range(0, H)]
    for j in range(0, H):
        partes = stdin.readline().split(' ')
	for k in range(0, W):
            inclinacion[j][k] = int(partes[k])
    for j in range(0, H):
	for k in range(0, W):
            base(mapa, inclinacion, j, k)
    print "Case #%d:" % (i + 1)
    for j in range(0, H):
	for k in range(0, W):
            stdout.write(mapa[j][k])
            if k != W - 1:
                stdout.write(" ")
	stdout.write("\n")
stdout.write("\n")
