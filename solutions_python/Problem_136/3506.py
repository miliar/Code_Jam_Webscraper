arq = open('B-small-attempt0.in', 'r')
cases = arq.readline()
dados = ""
C = 0
F = 0
X = 0
cont = 1

for linha in arq:
    achei = True
    qtdadeFazenda = 0
    casoTeste = 0
    casoAntes = 0
    cookiesPorSegundo = 2
    tempoCompraFazenda = 0
    primeiraVez = True
    fazendas = 0
    tempo = []
    #a,b,c = 0
    
    
    dados = linha.split()
    C = float(dados[0])
    F = float(dados[1])
    X = float(dados[2])
    
    casoAtual = X/2
    
    while achei:      
        casoTeste = 0
        
        if primeiraVez:
            tempo.append(0)
            primeiraVez = False
        else:
            tempo.append(C/(fazendas+2))
        fazendas =  qtdadeFazenda*F
        cookiesPorSegundo = 2 + fazendas
        
        qtdadeFazenda = qtdadeFazenda + 1
        
        tempoEspera = X/cookiesPorSegundo
        
        for i in tempo:
            casoTeste = casoTeste + i
        casoTeste = casoTeste + tempoEspera
        
        if casoTeste <= casoAtual:
            casoAtual = casoTeste
            
        else:
            achei = False    
            
    print casoAtual
    result = "Case #" + str(cont) + ": " + str(casoAtual) + '\n'
    arq_out = open('sample.out', 'a+')
    arq_out.write(result)
    cont = cont + 1