from numpy import *

def snapper_chain(N,K):
    state = zeros(N,dtype=bool)
    power = zeros(N,dtype=bool)
    power[0] = 1
    
    for k in range(K):
        state[power] = logical_not(state[power])
        M = argmin(state)
        if state[M] == False:
            power = concatenate([ones(M+1,dtype=bool),zeros(N-M-1,dtype=bool)])
        else:
            power = ones(N,dtype=bool)

    return logical_and(power[-1],state[-1])

if __name__ == "__main__":
    input = open("A-small-attempt0.in")
    T = int(input.readline())
    for t in range(T):
        N,K = [int(v) for v in input.readline().split()]
        if snapper_chain(N,K):
            print "Case #%d: ON"%(t+1)
        else:
            print "Case #%d: OFF"%(t+1)
