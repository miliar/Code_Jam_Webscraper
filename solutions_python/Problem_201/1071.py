from math import *;

def truc(N,K) :
    X = floor(log2(K))
    SSP = pow(2,X)
    SSP1 = pow(2,X+1)
    CSP = (N - (SSP-1)) // SSP
    CSP1 =(N - (SSP1-1)) // SSP1
    R = (N - (SSP - 1)) % SSP
    R1 = (N - (SSP1 - 1)) % SSP1

    if R == 0 :
        MIN = CSP//2-1 if CSP%2 == 0 else CSP//2
        MAX = CSP//2
    else :
        if K < SSP + R :
            if (CSP+1) % 2 == 1 :
                MIN = CSP//2
                MAX = CSP//2
            else :
                MIN = CSP//2
                MAX = CSP//2+1
        else :
            if CSP % 2 == 1 :
                MIN = CSP//2
                MAX = CSP//2
            else :
                MIN = CSP//2 - 1
                MAX = CSP//2

    return (MAX,MIN)

inputtamere = open("input","r")
f = inputtamere.readlines()

iTest = 0
f = f[1:]
for l in f :
    iTest += 1
    (n,k) = l.split()
    (max,min) = truc(int(n),int(k))

    print("Case #"+str(iTest)+": "+str(int(max))+" "+str(int(min)))
