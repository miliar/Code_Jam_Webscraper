import copy

def tryCutField(Field):
    emptyField=[]
    emptyField=copy.deepcopy(Field)
    highest=0
    different_values=[]
    #Tomo el mas alto de la lista Field y corto todo en emptyField
    for i in range(0,len(Field)):
        for j in range(0,len(Field[i])):
            #Si no esta el valor en mi lista lo agrego
            if not Field[i][j] in different_values:
                different_values.append(Field[i][j])
            if int(Field[i][j])>int(highest):
                highest=Field[i][j]
    for i in range(0,len(emptyField)):
        for j in range(0,len(emptyField[i])):
            emptyField[i][j]=highest

    #Ordeno los valores
    different_values.sort()
    different_values.reverse()
    canCut=True
    for i in range(1,len(different_values)):
        #Busco cual tiene ese valor
        for j in range(0,len(Field)):
            for k in range(0,len(Field[j])):
                if Field[j][k]==different_values[i] and emptyField[j][k]!=different_values[i]:
                    #Busco nros. mas grandes
                    canCut=True
                    for l in range(0,len(Field[j])):
                        if int(Field[j][l])>int(different_values[i]): #No se puede
                            canCut=False
                            break
                    if canCut==True:
                        for l in range(0,len(Field[j])):
                            emptyField[j][l]=different_values[i]
                    else:
                        canCut=True
                        for l in range(0,len(Field)):
                            if int(Field[l][k])>int(different_values[i]): #No se puede
                                canCut=False
                                break
                        if canCut==True:
                            for l in range(0,len(Field)):
                                emptyField[l][k]=different_values[i]
                    if canCut==False:
                        break
                        #else:
                        #    break
            if canCut==False:
                break

        return canCut


def output(status,caseNumber):
    fout=open("output.txt","a")
    fout.write("Case #"+str(caseNumber)+": "+status+"\n")
    fout.close()





isEOF=False
f=open("B-small-attempt4.in","r")
#f=open("test.in","r")
f.readline()
caseNumber=1
while isEOF==False:
    nSize=[]
    Field=[]
    partField=[]
    size=f.readline().strip()
    if not size:
        isEOF=True
    else:
        nSize=size.split(" ")
        for i in range(1,int(nSize[0])+1):
            n=f.readline().strip()
            partField=n.split(" ")
            Field.append(partField)
        #Verificar todos iguales
        areEqual=True
        for i in range(1,len(Field)):
            if Field[i] != Field[i-1]:
                    areEqual=False

        if int(nSize[0])==1 or areEqual==True:
            output("YES",caseNumber)
        else:
            if tryCutField(Field)==True:
                output("YES",caseNumber)
            else:
                output("NO",caseNumber)
        caseNumber=caseNumber+1



