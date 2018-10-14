def calculateSteps(initNum, destNum, max):
    if initNum == 1:
        return [max,0]
    
    pasos = 0
    fin = False
    valor = initNum
    while not fin:
        pasos += 1
        valor += (valor - 1)
        fin = valor > destNum
    return [pasos,valor]

def processData(fileName):
    f = open(fileName)
    
    T = int(f.readline().strip())
    
    for i in xrange(1, T+1):
        A,N = [int(var) for var in f.readline().strip().split(' ')]
        Motes = [int(var) for var in f.readline().strip().split(' ')]

        Motes.sort()

        valueOps = [0 for val in range(len(Motes))]
        ops = 0
        lastChange = -1
        for j in xrange(len(Motes)):
            if A <= Motes[j]:
                
                if lastChange >= 0:
                    if valueOps[lastChange] > (j - lastChange):
                        lastChange = j
                    else:
                        valueOps[lastChange] == len(Motes) - lastChange
                        break
                data = calculateSteps(A,Motes[j],len(Motes) - j)
                if data[0] >= len(Motes) - j:
                    valueOps[j] = len(Motes) - j
                    break
                else:
                    valueOps[j] = data[0]
                    A = data[1] + Motes[j]
            else:
                A += Motes[j]
        
                
        #print valueOps
        print "Case #" + str(i) + ': ' + str(sum(valueOps))




#processData('prueba.in')
processData('A-small-attempt1.in')
