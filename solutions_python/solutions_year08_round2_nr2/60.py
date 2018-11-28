#-*- coding: utf-8 -*-
import sys


def primes(n):
    if n < 2: return []
    if n == 2: return [2]
    s = range(3, n, 2)
    mroot = n ** 0.5
    half = len(s)
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m * m - 3)//2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m

        i = i + 1
        m = 2 * i + 3
    return [2]+[x for x in s if x]

def generar_conjuntos(a, b):
    d = {}
    for num in range(a, b+1):
        d[num] = set([num])
    return d

def comparten(a, b, p, primos):
    for primo in primos:
        if (primo >= p) and (a%primo == 0) and (b%primo == 0):
            return True
    return False

if __name__ == '__main__':
    file_name = sys.argv[1]

    input_file = open(file_name).readlines()
    output_file = open('output.ou', 'w')


    
    N = int(input_file[0])
    input_file = input_file[1:]
    for case in range(1, N+1):
        A, B, P = input_file[0].split()
        A = int(A)
        B = int(B)
        P = int(P)
        input_file = input_file[1:]

        conjuntos = generar_conjuntos(A, B)
        primos = primes(B/2)
        for a in range(A, B+1):
            for b in range(a+1, B+1):
                if comparten(a, b, P, primos):
                    conjuntos[a] = conjuntos[a].union(conjuntos[b])
                    conjuntos[b] = conjuntos[a]

        #filtrado
        
        for conjunto in conjuntos.keys():
            for ind2 in conjuntos.keys():
                if conjunto == ind2:
                    continue
                try:
                    if not (conjuntos[conjunto].intersection(conjuntos[ind2]) == set([])):
                        conjuntos.pop(conjunto)
                except:
                    pass
        
        output_file.write("Case #%d: %d\n"%(case, len(conjuntos.keys())))

