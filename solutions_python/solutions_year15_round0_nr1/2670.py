# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 10:46:25 2015

@author: Jose
"""

amigos_casos = []
    
with open('A-large.in') as f_in:
    T = int(f_in.readline())
    for t in range(T):
        S, p = f_in.readline().split()
        S_max = int(S)
        audiencia = [int(c) for c in p]
        amigos = 0
        for i in range(1, S_max + 1):
            audiencia_levantada = sum(audiencia[:i]) + amigos
            if i > audiencia_levantada:
                amigos += i - audiencia_levantada
        amigos_casos.append(amigos)
        
with open('output_large.out', 'w') as f_out:
    for ac in range(len(amigos_casos)):
        f_out.write('Case #{}: {}\n'.format(ac + 1, amigos_casos[ac]))
        