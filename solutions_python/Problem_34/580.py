linha = raw_input()
linha = linha.split(" ")
L = int (linha[0])
D = int (linha[1])
N = int (linha[2])
case = 0

x = D
dicionario = []
while (x != 0) :
    x -= 1
    dicionario.append(raw_input())
    
while (case <= N) :
    case += 1    
    
    palavra = raw_input()
    
    separar = False
    matriz = []
    lista = []
    junto = ''
    for l in palavra :
        if l is "(" :
            separar = True
            if junto != '' :
                matriz.append(junto)
                junto = ''
        elif l is ")" :
            separar = False
            matriz.append(lista)
            lista = []
        elif (separar == True) :
            lista.append(l)
        elif (separar == False) :
            junto += l
    
    if (separar == False) :
        matriz.append(junto)
    
    total = 0
    erro = True
    for i in range(0,len(dicionario)) :
        x = 0
        matrizDic = []
        junto = ''
        for elemento in dicionario[i] :
            if type(matriz[x]) is list :
                matrizDic.append(elemento)
                x += 1
            else :
                junto += elemento
                if (len(matriz[x]) == len(junto)) :
                    matrizDic.append(junto)
                    junto = ''
                    x += 1
                    
        if (junto != '') :
            matrizDic.append(junto)
            
        for j in range(0,len(matrizDic)) :
            if type(matriz[j]) is list :
                if matrizDic[j] in matriz[j] :
                    erro = False
                else :
                    erro = True
                    break
            else :
                if matrizDic[j] == matriz[j] :
                    erro = False
                else :
                    erro = True
                    break
                
        if erro == False :
            total += 1
    saida = "Case #"+case+": "+total
    print saida