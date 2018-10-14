CurrentPathIn = "input"
CurrentPathOut = "output"

fr = open(CurrentPathIn,"r")
fw = open(CurrentPathOut,"w")

def glue(S, T, X, p, tot):
    n = len(X)
    I = []
    L = []
    for i in range(n-1):
        if X[i] == X[i+1] and X[i] == p:
            I.append(i)
            L.append(S[i+1] - T[i])
    if X[n-1] == X[0] and X[0] == p:
        I.append(n-1)
        L.append(1440 - T[n-1] + S[0])
        
    k = len(I)
    if k == 0:
        return tot

    I, L = zip(*sorted(zip(I,L), key = lambda x: x[1]))
    for i in range(k):
        if tot+L[i] > 720:
            break
        else:
            tot+=L[i]
            if I[i]!=n-1:
                T[I[i]] = S[I[i]+1]
            else:
                T[n-1] = 1440
                S[0] = 0

    return tot

        
qwe = int(fr.readline())
for t in range(qwe):
    n0, n1 = list(map(int, fr.readline().split()))
    n = n0 + n1;
    S = [0]*n
    T = [0]*n
    X = [0]*n
    tot = [0]*2
    for i in range(n0):
        S[i], T[i] = list(map(int, fr.readline().split()))
        X[i] = 0
        tot[0] += T[i] - S[i]
    for i in range(n0, n):
        S[i], T[i] = list(map(int, fr.readline().split()))
        X[i] = 1
        tot[1] += T[i] - S[i]

    ###
    S, T, X = zip(*sorted(zip(S, T, X), key = lambda x: x[0]))
    S = list(S)
    T = list(T)
    X = list(X)
    print(S, T, X, tot)
    tot[0] = glue(S, T, X, 0, tot[0])
    tot[1] = glue(S, T, X, 1, tot[1])
    print(S, T, X, tot)
    res = 0
    for i in range(n-1):
        if X[i]!=X[i+1]:
            res+=1
        else:
            if T[i] != S[i-1]:
                res+=2
    if X[n-1]!=X[0]:
        res+=1
    else:
        if (T[n-1] == 1440 and S[0]==0):
            pass
        else:
            res+=2

    ###
    res = str(res)
    
    print("Case #"+str(t+1)+": "+res+"\n")
    fw.write("Case #"+str(t+1)+": "+res+"\n")

fr.close()
fw.close()
