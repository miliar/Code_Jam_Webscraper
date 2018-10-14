from sys import argv
from collections import Counter

script, filename = argv

txt = open(filename)

casos = int(txt.readline())

def substituiNaLinha(linha):
    #print "sss", linha
    usarLetra = False
    novaLinha = ""
    for letra in linha:
        if letra != "?":
            usarLetra = letra
            novaLinha = novaLinha.replace("*",usarLetra)
            novaLinha += usarLetra
        elif letra == "?":
            if usarLetra != False:
                novaLinha = novaLinha.replace("*",usarLetra)
                novaLinha += usarLetra
            else:
                novaLinha += "*"
    return novaLinha
            

def cake():
    R, C = map(int,txt.readline().strip().split())
    cols=[]
    saida=[]
    novoCols = []
    linha = 0
    for i in xrange(R):
        cols.append(txt.readline().strip())
    cnts = [Counter(s) for s in cols]
    usarLinha = 0
    if len(cnts[0]) == 1 and cnts[0]["?"] > 0:
        for cnt in cnts:
            if (len(cnt) > 1 ) or (len(cnt) == 1 and cnt["?"] == 0):
                break
            else:
                usarLinha += 1
        for i in range(usarLinha+1):
            #print i, cols[i], cols[usarLinha]
            novoCols.append(cols[usarLinha])
        for i in range (usarLinha + 1, len(cols)):
            novoCols.append(cols[i])
        #print novoCols
        cnts = [Counter(s) for s in novoCols]
    else:
        novoCols = cols
    for cnt in cnts:
        if cnt["?"] == 0: #nao tem ?
            saida.append(novoCols[linha])
        elif len(cnt) == 1 and cnt["?"] > 0: #so tem ?
            if linha == 0:
                linha = linha
            else:
                saida.append (saida[linha - 1])
        else:
            novaLinha = substituiNaLinha(novoCols[linha])
            saida.append(novaLinha);
                    
                
        linha += 1
    for i in saida:
        print "".join(map(str,i))

for case in range(1,casos+1):
    print 'Case #%d:' % case
    cake()