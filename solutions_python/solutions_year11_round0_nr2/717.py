def solvecase(L):
    C = int(L[0])
    D = int(L[C+1])
    N = int(L[C+D+2])

    F = L[1:C+1]
    X = L[C+2:C+D+2]
    S = L[-1]

    Q = []

    for s in S:
        #get spell from list
        Q.append(s)
        #send recent spells to check combination
        if len(Q) > 1:
            comb = chkcombine(F,Q[-1],Q[-2])
            if comb!=None:
                Q.pop()
                Q.pop()
                Q.append(comb)
            #check for opposing spells
            for i in range(len(Q)-1):
                if chkoppose(X,Q[i],Q[-1]):
                    #destroy everything
                    Q = []
                    break
    return Q

def chkcombine(formulalist,s1,s2):
    for formula in formulalist:
        if (formula[0]==s1 and formula[1]==s2) or (formula[1]==s1 and formula[0]==s2):
            return formula[2]
    return None

def chkoppose(opposelist,s1,s2):
    for oppose in opposelist:
        if (oppose[0]==s1 and oppose[1]==s2) or (oppose[1]==s1 and oppose[0]==s2):
            return True
    return False
    

N = int(input())

for n in range(N):
    r = solvecase(input().split(' '))
    
    print("Case #",str(n+1),": [",sep='',end='')
    print(", ".join(r),sep='',end='')
    print(']')
