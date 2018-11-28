'''
Created on 08/05/2010

@author: kivson
'''

def main():
    with file("A-large.in",'r') as entrada :
        saida = file("out.txt","w")
        instancia = 1
        qtdInstancias = int(entrada.readline())
        for i in xrange(qtdInstancias):
            fin = entrada.readline().split()
            snappers = int(fin[0])
            estalos = int(fin[1])
            if (estalos + 1) % (2 ** snappers) == 0:
                acendeu = "ON"
            else:
                acendeu = "OFF"
            print >> saida , "Case #%d: %s" % (instancia, acendeu)
            instancia += 1
        
if __name__ == '__main__':
    main()