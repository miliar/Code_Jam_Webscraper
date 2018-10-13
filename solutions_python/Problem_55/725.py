'''
Created on 07/05/2010

@author: kivson
'''
from itertools import cycle
def main():
    inp = file("C-small-attempt1.in")
    saida = file("out.txt",'w')
    instancia = 1
    total = int (inp.readline())
    for i in xrange(total):
        ganho = 0
        capacidadeAtual = 0
        entrada = inp.readline().split()
        voltas = int(entrada[0])
        capacidade = int(entrada[1])
        totalGrupos = int(entrada[2])
        fila = [int(x) for x in inp.readline().split()]
        capacidadeAtual = capacidade      
        gruposDentro = 0
        i = 0
        while True :
            if not voltas:
                break
            grupo = fila[i]
            if capacidadeAtual >= grupo and gruposDentro < totalGrupos:
                gruposDentro += 1
                capacidadeAtual -= grupo
                ganho += grupo
                fila.append(grupo)
                i += 1
            else:
                gruposDentro = 0
                voltas -= 1
                capacidadeAtual = capacidade
        print >> saida, "Case #%d: %d" % (instancia,ganho)
        instancia += 1
    saida.close()

if __name__ == '__main__':
    main()