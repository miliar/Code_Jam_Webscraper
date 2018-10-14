#!/usr/bin/env python

def case(T):
    K, N = map(int, input().split()) 
    T = float(input())
    cores = [float(i) for i in input().split()]
    while T > 0:
        cores = sorted(cores)
        diffl = sorted(list(set(cores)))
        if len(diffl) >= 2:
            diff = diffl[1] - diffl[0]
        else:
            for i in range(len(cores)):
                cores[i] += T/len(cores)
            return prob(cores)
        nr = cores.count(cores[0])
        #print(T, cores, diff, nr)
        if nr*diff > T:
            diff = T/nr
        T -= diff*nr
        for i in range(nr):
            cores[i] += diff
    return prob(cores)

def prob(l):
    c = 1
    for i in l:
        c *= i
    return c

if __name__=="__main__":
    for i in range(int(input())):
        print("Case #{}: {}".format(i+1, case(i)))
