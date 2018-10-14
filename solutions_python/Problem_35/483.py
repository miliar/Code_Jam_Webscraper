def pegaGrupo(x) :
    if vetor[x] == x :
        return x
    return pegaGrupo(vetor[x])

N = input()
case = 0

while case < N :
    case += 1
    linha = raw_input()
    linha = linha.split(" ")
    
    H = int(linha[0])
    W = int(linha[1])
    
    matriz = [0] * H
    for i in range(0, len(matriz)) :
        matriz[i] = raw_input()
        matriz[i] = matriz[i].split(" ")
        for j in range(0, len(matriz[i])) :
            matriz[i][j] = int(matriz[i][j])
    
    vetor = [-1]*(H*W)
    
    for i in range(0, len(matriz)) :
        for j in range(0, len(matriz[i])) :
            cima = W * (i-1) + j
            baixo = W * (i+1) + j
            esquerda = W * (i) + (j-1)            
            direita = W * (i) + (j+1)
            
            grupo = matriz[i][j]
            v = W * (i) + j
            if (0 <= cima < W * H and i-1 >= 0) :
                if (grupo > matriz[i-1][j]) :
                    grupo = matriz[i-1][j];
                    v = W * (i-1) + j
            if (0 <= esquerda < W * H and j-1 >= 0) :
                if (grupo > matriz[i][j-1]) :
                    grupo = matriz[i][j-1]
                    v = W * (i) + j-1
            if (0 <= direita < W * H  and j+1 < W) :
                if (grupo > matriz[i][j+1]) :
                    grupo = matriz[i][j+1]
                    v = W * (i) + j+1
            if (0 <= baixo < W * H  and i+1 < H) :
                if (grupo > matriz[i+1][j]) :
                    grupo = matriz[i+1][j]
                    v = W * (i+1) + j
                    
                    
            vetor[W * (i) + j] = v   
            
    for i in range(0, len(matriz)) :
        for j in range(0, len(matriz[i])) :
            vetor[W * (i) + j] = pegaGrupo(W * (i) + j)
            
    pais = list(set(vetor))
    pais.sort()
    letra = ord("a")
    for elemento in pais :
        i = elemento / W
        j = elemento % W    
        if (elemento != pegaGrupo(0)) :
            letra = letra + 1
            matriz[i][j] = chr(letra)
        else :
            matriz[i][j] = "a"
    
    for i in range(0, len(matriz)) :
        for j in range(0, len(matriz[i])) :
            pi = vetor[W * i + j] / W
            pj = vetor[W * i + j] % W
            matriz[i][j] = matriz[pi][pj]            
         
    saida = "Case #"+str(case)+": "
    print saida
    for i in range(0, len(matriz)) :
        for j in range(0, len(matriz[i])) :
            print matriz[i][j],
        print ''   
                 