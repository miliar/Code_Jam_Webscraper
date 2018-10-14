def contain(matriz, char):
    for r in matriz:
        if char in r:
            return True
    
    return False

def print_mat(matriz):
    for r in matriz:
        print(''.join(r))

def change_direita(matriz, char, r, c):
    lim = len(matriz[0]) - 1
    while c<lim and matriz[r][c+1] == '?':
        c += 1
        matriz[r][c] = char
        
def change_esquerda(matriz, char, r, c):
    lim = 0
    while(c > lim and matriz[r][c-1] == '?'):
        c -= 1
        matriz[r][c] = char

def change_cima(matriz, char, r, c):
    lim = 0
    while (r > lim and matriz[r-1][c] == '?'):
        r -= 1
        matriz[r][c] = char

def change_baixo(matriz, char, r, c):
    lim = len(matriz) -1
    while(r<lim and matriz[r+1][c] == '?'):
        r+=1
        matriz[r][c] = char

def change_matriz(matriz, vlr):
    for r in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[r][c] != '?':
                if vlr % 2 == 0:
                    change_direita(matriz, matriz[r][c], r, c)
                    change_esquerda(matriz, matriz[r][c], r, c)
                else:
                    change_cima(matriz, matriz[r][c], r, c)
                    change_baixo(matriz, matriz[r][c], r, c)



def answer():
    r,c = [int (s) for s in input().split(' ')]

    mat = []
    for i in range(r):
        mat.append(list(input()))
    
    vlr = 1
    while contain(mat,'?'):
        change_matriz(mat, vlr)
        vlr+= 1

    print_mat(mat)



times = int(input())

for t in range(1,times + 1):

    print('Case #{}:'.format(str(t)))
    answer()
