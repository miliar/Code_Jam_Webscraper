from __future__ import division
from operator import itemgetter


def main():
    entrada=open('A-large.in', 'r')
    saida=open('superl.out','w')
    casos = int(entrada.readline())
    for i in range(1,casos+1):
        nomes = []
        palavras = []
        zero = False
        
        motores = int(entrada.readline())
        for j in range(motores):
            nomes.append(entrada.readline().strip('\n'))

        #print nomes
        
        consultas = int(entrada.readline())
        for j in range(consultas):
            palavras.append(entrada.readline().strip('\n'))

        menor = 10000
        emenor = nomes[0]
        contagem = {}
        for motor in nomes:
            contagem[motor] = palavras.count(motor)
            if contagem[motor] < menor:
                menor = palavras.count(motor)
                emenor = motor


        for ind in range(len(palavras)-1):
            if palavras[ind] == palavras[ind+1]:
                contagem[palavras[ind]]=contagem[palavras[ind]]-1


        for motor in nomes:
            if motor not in palavras:
                saida.write("Case #%i: 0\n" % i)
                zero = True
                break

        if not zero:
            totals = sorted(contagem.iteritems())

            switches = 0
            current = 0
            #primeira = {}
            oldmotor = None
            while current < len(palavras):
                primeira = {}
                #a = raw_input()
                for motor in nomes:
                    if motor == oldmotor:
                        continue
                    if motor in palavras[current:]:
                        primeira[motor] = palavras[current:].index(motor)
                    else:
                        primeira[motor] = 99999

                primeiras = sorted(primeira.iteritems(), key=itemgetter(1), reverse=True)
                #print primeiras
                current += primeiras[0][1]
                switches+=1
                oldmotor = primeiras[0][0]
          
            saida.write("Case #%i: %i\n" % (i, switches-1)) 
            print "Caso #%i" % i
            #print "%i %i %i" %(totals[0][1],totals2[0][1],totals3[0][1])
        #print contagem      
        #print menor

      
    entrada.close()
    saida.close()
    print "Tchau e obrigado pelos peixes!"

main()
