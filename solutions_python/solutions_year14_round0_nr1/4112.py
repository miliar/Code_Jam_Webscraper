arquivo = open("a-magictrick.txt")
arquivo = arquivo.read()
arquivo = arquivo.split("\n")
    
t = int(arquivo[0])
i = 0
x3 = 0
x6 = 0
while i < t:
    linha1 = [int(arquivo[1 + x3]), 1+x3]
    matriz1, matriz2 = [],[]
    
    for j in range(4):
        n = arquivo[2 +x3 + j]
        matriz1.append(n)
        matriz1[j] = matriz1[j].split(" ")

    linha2 = [int(arquivo[6 + x6]),6+x6]
              
    
    for j in range(4):
        n = arquivo[7 +x6 + j]
        matriz2.append(n)
        matriz2[j]= matriz2[j].split(" ")

    contador = 0
    for k in matriz1[linha1[0]-1]:
        for j in matriz2[linha2[0]-1]:
            if k == j and k != " " and int(k) > 0 and int(k) < 17:
                contador += 1
                if contador == 1:
                    valor = k
                    valor2 = j
                    

    x3 += 10
    x6 += 10
    i += 1
    
    if contador == 1:
        print("Case #%d"%i, end="")
        print(":", valor)
    if contador > 1:
        print("Case #%d"%i, end="")
        print(": Bad magician!")
    if contador < 1:
        print("Case #%d"%i, end="")
        print(": Volunteer cheated!")
    
    
