fit = open('A-small-attempt0.in','r')
lineas=fit.readlines()
#print(lineas)
#patrocinado por monster y kebab XD
intro = True
pos = []
matrix = []

repeticions = 0

matriuI = 0
matriuF = 4

posicioI = 0

archi=open('datos.in','w')

for li in lineas:
    if lineas[0] == li and intro:
        intro = False
        repeticions = li
    elif len(li) <= 3:
        pos.append(li.split())
    elif len(li) > 3:
        matrix.append(li.split())
        #print(matrix)


def cartaResult(matrix,matrix2,pos,pos2):
    count = 0
    resposta = 0
    for i in matrix[int(pos)-1]:
        for j in matrix2[int(pos2)-1]:
            if j == i:
                count += 1
                resposta = j

    if count == 1:
        return resposta
    elif count > 1:
        return 'Bad magician!'
    elif count == 0:
        return 'Volunteer cheated!'

def calcul():
    global repeticions,matriuI,matriuF,posicioI,pos
    for i in range(int(repeticions)):
        
        matriu = matrix[matriuI:matriuF]
        matriu2 = matrix[matriuI+4:matriuF+4]
        pos1 = pos[posicioI][0]
        pos2 = pos[posicioI+1][0]
        resultat = cartaResult(matriu,matriu2,pos1,pos2)
        
        archi.write('Case #'+str(i+1)+': '+str(resultat)+'\n')
        
        matriuI += 8
        matriuF += 8
        posicioI += 2
    return archi.close()
calcul()
        


