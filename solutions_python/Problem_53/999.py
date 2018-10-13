fonte = open('c:\\inputSnapper.in', 'r')
saida = open('c:\\outputSnapper.out','w')

T = 0

N = 0
K = 0
snappers = []
rodadas = 0

T = int(fonte.readline().strip())
for i in xrange(1,T+1):
    snappers = []
    linha = fonte.readline().strip()
    numeros = linha.split()
    
    number = int(numeros[0])
    clicks = int(numeros[1])
    #print str(i)
    
    
    for j in xrange(0,number):
        snappers.append(0)
        
    while (clicks>0):
        pos = 0
        rodadas = rodadas + 1 
        while (pos<number):
            if snappers[pos] == 0:
                snappers[pos] = 1
                break
            else:
                snappers[pos] = 0
                
            pos = pos + 1
        #if pos == number:
        #    while clicks >= rodadas:
        #        clicks = clicks - rodadas
        #    rodadas=0
        #    clicks = clicks + 1 

        clicks = clicks - 1
    
    ligado = True
    for j in xrange(0,number):
        if snappers[j] == 0:
            ligado = False

    if ligado:
        string = 'Case #'+str(i)+': ON '
    else:
        string = 'Case #'+str(i)+': OFF '
    saida.write(string+'\n')
    #print string
    
saida.close()
fonte.close()    



