#!/usr/bin/env python

# -------------------------------
# MagicTrick
# Raul B. Barbosa
# -------------------------------

import sys

def main():
    
    solve(sys.stdin, sys.stdout)
    

def read_problem(r,dados):
    """
    r is a reader
    dados is a bunch of dados, rs
    """
    primeira_linha = r.readline()
    primeira_linha = int(primeira_linha)
    
    primeira_resposta = [[i for i in range(0,4)] for x in range(0,4)]
    for i in xrange(0,4):
        line = r.readline()
        primeira_resposta[i] = [int(j) for j in line.split()]
    
    segunda_linha = r.readline()
    segunda_linha = int(segunda_linha)
    
    segunda_resposta = [[i for i in range(0,4)] for x in range(0,4)]
    for i in xrange(0,4):
        line = r.readline()
        segunda_resposta[i] = [int(j) for j in line.split()]
    
    dados[0] = [primeira_linha,segunda_linha]
    dados[1] = [primeira_resposta,segunda_resposta]
    
    
def eval_problem(linha, matrizes):
    """
    
    """
    
    pri_m = matrizes[0]
    seg_m = matrizes[1]
    pri_l = linha[0] - 1 
    seg_l = linha[1] -1
    
    linha = [i for i in pri_m[pri_l] ]
    linha2 = [i for i in seg_m[seg_l]]
    
    result = 0
    carta = 0
    for i in linha:
        for j in linha2:
            if i == j:
                result = result+1
                carta = i
    return (result,carta)
    
def print_problem(w, vez, result, carta):
    """
    
    """

    if result == 0:
        w.write("Case #"+str(vez)+": Volunteer cheated!\n")
    if result == 1:
        w.write("Case #"+str(vez)+": "+str(carta)+"\n")
    if result > 1:
        w.write("Case #"+str(vez)+": Bad magician!\n")
    

def solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    
    test_cases = r.readline()
    test_cases = int(test_cases)
    
    for test_case in xrange(0,test_cases) :
        dados = [1,2]
        read_problem(r, dados)
        result,carta = eval_problem(dados[0],dados[1])
        print_problem(w, test_case+1, result, carta)
    
    

if __name__ == "__main__":
    main()


