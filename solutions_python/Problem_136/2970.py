#!/usr/bin/env python

# -------------------------------
# Cookie Whatever 
# Raul B. Barbosa
# -------------------------------

import sys

def main():
    
    solve(sys.stdin, sys.stdout)
    

def read_problem(r,dados):
    """
    r is a reader
    dados is a bunch of dados, lol
    """
    s = r.readline()
    assert s != ""
    l_a = s.split()
    dados[0] = float(l_a[0])
    dados[1] = float(l_a[1])
    dados[2] = float(l_a[2])
    
def eval_problem(farm_cost, farm_prod_inc, goal):
    """
    
    """
    pr_i = 2.0
    
    cookies = 0
    
    tempo_ate_fabrica = [ 0 for i in xrange(0,1000000)]
    custo_sol_fabrica = [ 0 for i in xrange(0,1000000)]
    for i in xrange(1,1000000):
        tempo_ate_fabrica[i] = tempo_ate_fabrica[i-1] + farm_cost/(2+farm_prod_inc*(i-1))
    
    for i in xrange(0,1000000):
        custo_sol_fabrica[i] = tempo_ate_fabrica[i] + goal/(2+farm_prod_inc*i)
    
    return min(custo_sol_fabrica)
    
def print_problem(w, vez, result):
    """
    
    """    
    w.write("Case #"+str(vez)+": "+str(result)+"\n")
    

def solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    
    test_cases = r.readline()
    test_cases = int(test_cases)
    
    for test_case in xrange(0,test_cases) :
        dados = [1,2,3]
        read_problem(r, dados)
        v = eval_problem(dados[0],dados[1],dados[2])
        print_problem(w, vez=test_case+1, result=v)
    
    

if __name__ == "__main__":
    main()


