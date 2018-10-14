'''
Created on 13/04/2012

@author: david
'''
GOOGLERESE_LANGUAGE = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
                       "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                       "de kr kd eoya kw aej tysr re ujdr lkgc jv",
                       "y qee z"]

ENGLISH_LANGUAGE = ["our language is impossible to understand",
                    "there are twenty six factorial possibilities",
                    "so it is okay if you want to just give up",
                    "a zoo q"]

ENGLISH_ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def obtenAlfabeto():
    aux1 = []
    aux2 = []
    lenguaje = []
    auxCad = ""
    auxCad2 = ""
    for cad in GOOGLERESE_LANGUAGE:
        auxList = cad.split(" ")
        aux1.append(auxList)
    for cad in ENGLISH_LANGUAGE:
        auxList = cad.split(" ")
        aux2.append(auxList)
    for i in range(len(aux1)):
        for j in range(len(aux1[i])):
            for k in range(len(aux1[i][j])):
                pos = auxCad.find(aux1[i][j][k]) 
                if pos ==-1:
                    auxCad += aux1[i][j][k]
                    auxCad2 += aux2[i][j][k]
    for i in ENGLISH_ALPHABET:
        if auxCad.find(i) == -1:
            if auxCad2.find(i) == -1:
                auxCad += i
                auxCad2 += i
                
            else:
                for j in cad:
                    if auxCad2.find(j) ==-1:
                        auxCad += i
                        auxCad2 += j
    lenguaje.append(auxCad)
    lenguaje.append(auxCad2)
    return lenguaje           
    

if __name__ == "__main__":
    language = []
    fileIn = open("A-small-attempt2.in")
    fileOut = open("A-small-attempt2.out",'w')
    iter = int (fileIn.readline())
    l = range(iter)
    language = obtenAlfabeto()
    for i in l:
        cad = fileIn.readline()
        cad = cad[:-1]
        auxList = cad.split(" ")
        convertCad = ""
        for word in auxList:
            for letter in word:
                pos = language[0].find(letter)
                convertCad += language[1][pos]
            convertCad += " "
        convertCad = convertCad[:-1]
        fileOut.writelines("Case #%d: %s" % (i + 1, convertCad)+'\n')  
    fileIn.close()
    fileOut.close()
    
    
    
    