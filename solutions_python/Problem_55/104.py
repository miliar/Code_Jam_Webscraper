#! /usr/bin/env python

import sys, math, copy


def slow_method(N,K,g):
    total_profit  = 0
    len_g = len(g)
    def inc_j(k):
        if k < len_g-1:
            return k + 1
        else :
            return 0
    j = -1
    for i in range(N):
        j = inc_j(j)
        j_start = j
        passengers = g[j]
        while passengers + g[inc_j(j)] <= K and inc_j(j) <> j_start:
            j = inc_j(j)
            passengers =  passengers + g[j]
        #print(passengers)
        total_profit = total_profit +  passengers*1
    return total_profit 


def quick_method(N,K,g):
    total_profit  = 0
    len_g = len(g)
    def next_j(k):
        if k < len_g-1:
            return k + 1
        else :
            return 0
    j = -1
    #looks for repeating cycles.
    j_hist = []
    profit_hist = []
    while next_j(j) not in j_hist and len(j_hist) < N:
        j = next_j(j)
        j_start = j
        passengers = g[j]
        while passengers + g[next_j(j)] <= K and next_j(j) <> j_start:
            j = next_j(j)
            passengers =  passengers + g[j]
        #print(passengers)
        j_hist.append(j_start)
        profit_hist.append( passengers*1)
    if len(j_hist) == N:
        return sum(profit_hist)
    else :
        j_rep = next_j(j) #leading elements before cycle
        index = j_hist.index(j_rep)
        profit = sum(profit_hist[:index])
        j_cycle = j_hist[index:]
        profit_cycle = profit_hist[index:]
        N_rem = N - index
        whole_cycles = N_rem/len(j_cycle)
        part_cycle = N_rem- whole_cycles*len(j_cycle)
        #print('  No runs=%i,cycle len %i, whole_cycles %i, part_cycle %i' % 
        #      (N,len(j_hist), whole_cycles, part_cycle))
        return profit + sum(profit_cycle)*(whole_cycles) + sum(profit_cycle[:part_cycle])

#main code    
f = file(sys.argv[1])
lines = f.readlines()
f.close()

T = int(lines[0].strip())
results = []
debug = False

for i in range(T):
    N,K,r = [ int(j) for j in lines[i*2+1].split(' ')]
    g = [ int(j) for j in lines[i*2+2].split(' ')]
    results.append(quick_method(N,K,copy.copy(g)))
    print('case (%i of %i) : N %i, K %i, profit %i' % (i+1, T, N, K, results[-1]))
    if debug : #checking
        qmv = results[-1]
        smv = slow_method(N,K,copy.copy(g))
        if qmv <> smv:
            print(N,K,g)
            raise ValueError,'slow method does not correspond to quick method! quick method %i, slow_method %i' % (qmv, smv)


#writing output file
f = file(sys.argv[1].replace('.in','.out'),'w')
f.write('\n'.join(['Case #%i: %i' % (i+1,s) for i,s in enumerate(results) ]))
f.close()
