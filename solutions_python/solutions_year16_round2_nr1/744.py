import numpy as np
import time
from scipy.linalg import circulant

#f = open('A-sample.in','r')
#g = open('A-sample.ou','w')

#f = open('A-small-attempt1.in','r')
#g = open('A-small.ou','w')

f = open('A-large.in','r')
g = open('A-large.ou','w')


def inputToList(f):
    n = int(f.readline()[:-1])
    iL = []
    for k in range(n):
        iL += [f.readline()[:-1]]
    return iL


iL = inputToList(f)


def solution(pat):
    n = len(pat)
    Z = 0
    E = 0
    R = 0
    O = 0
    N = 0
    T = 0
    W = 0
    H = 0
    U = 0
    F = 0
    I = 0
    V = 0
    S = 0
    X = 0
    G = 0
    for k in range(n):
        if pat[k] == 'Z':
            Z += 1
        elif pat[k] == 'E':
            E += 1
        elif pat[k] == 'R':
            R += 1
        elif pat[k] == 'O':
            O += 1
        elif pat[k] == 'N':
            N += 1
        elif pat[k] == 'T':
            T += 1
        elif pat[k] == 'W':
            W += 1
        elif pat[k] == 'H':
            H += 1
        elif pat[k] == 'U':
            U += 1
        elif pat[k] == 'F':
            F += 1
        elif pat[k] == 'I':
            I += 1
        elif pat[k] == 'V':
            V += 1
        elif pat[k] == 'S':
            S += 1
        elif pat[k] == 'X':
            X += 1
        elif pat[k] == 'G':
            G += 1
    N_0 = Z
    N_2 = W
    N_4 = U
    N_8 = G
    N_6 = X
    N_3 = H - G
    N_7 = S - X
    N_5 = V - N_7
    N_9 = I - N_6 - N_5 - N_8
    N_1 = O - N_0 - N_2 - N_4
    N = [N_0,N_1,N_2,N_3,N_4,N_5,N_6,N_7,N_8,N_9]
    return N

def solutionToString(sol):
    s = ''
    for k in range(len(sol)):
        for i in range(sol[k]):
            s+=str(k)
    return s



def outputList(iL):
    oL = []
    for k in range(len(iL)):
        oL += [solution(iL[k])]
	print k+1,'Done'
    return oL


oL = outputList(iL)


def outputListToString(oL):
    oS = ''
    for k in range(len(oL)):
        oS += 'Case #'+str(k+1)+': '+ solutionToString(oL[k])+'\n'
    return oS


oS = outputListToString(oL)


g.write(oS)


g.close()
