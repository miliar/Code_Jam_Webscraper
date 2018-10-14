'''
Created on 13/04/2013

@author: Carles
'''

def compruebaFila(cesped,n,alt,vh):
    #print cesped[n]
    if vh: #fila
        maximo = max(cesped[n])
        #print maximo
        if maximo > alt:
            return False
        for i in range(len(cesped[n])):
            if cesped[n][i]<alt:
                if not compruebaFila(cesped,i,cesped[n][i],not vh):
                    return False
        return True
    
    else: # columna
        col = []
        for i in range(len(cesped)):
            col.append(cesped[i][n])
        maximo = max(col)
        #print maximo
        if maximo > alt:
            return False
        for i in range (len(col)):
            if col[i]<alt:
                if not compruebaFila(cesped, i, col[i], not vh):
                    return False
        return True
        


def trataCaso(inFile):
    linea = inFile.readline()
    n = int(linea.partition(' ')[0])
    m = int(linea.partition(' ')[2])
    
    if n == 1 or m == 1:
        for i in range(n):
            inFile.readline()
        return True
    
    cesped = [None]*n
    for i in range(n):
        cesped[i] = [None]*m
        linea = inFile.readline()
        for j in range(m):
            cesped[i][j] = int(linea.partition(' ')[0])
            linea = linea.partition(' ')[2]
        #print cesped[i]

    #maximo = 0       
    #for i in range(n):
    #    if max(cesped[i])>maximo:
    #        maximo = max(cesped[i])
        
    posible = True
    for i in range(n):
        if not compruebaFila(cesped,i,max(cesped[i]),True):
            posible = False
            break;
        
    return posible


def main():
    inFile = open('input.in', 'r')
    outFile = open('output.out', 'w')

    numCasos = int(inFile.readline())

    for i in range(numCasos):
        if trataCaso(inFile):
            outFile.write("Case #"+str(i+1)+": YES\n")
            print "Case #"+str(i+1)+": YES\n"
        else:
            outFile.write("Case #"+str(i+1)+": NO\n")
            print "Case #"+str(i+1)+": NO\n"
        
        
if __name__ == "__main__":main()