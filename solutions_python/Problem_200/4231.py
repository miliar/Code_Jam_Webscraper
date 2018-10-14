def check(L):
    for i in range(0, len(L)-1):
        if L[i] > L[i+1]:
            return i+1
    return -1

def operate(n):
    I = check(n)
    for i in range(I,len(n)):
        n[i] = 9
    n[I-1]-=1
    return n

T = int(input())

for t in range(T):
    
    LstrN = list(input())
    A = N = int( ''.join(LstrN) )
    LintA = [int(x) for x in LstrN]
    
    while True:
        if check(LintA) == -1 and  A <= N:
            print ("Case #"+str(t+1)+":", A)
            break
        else:
            LintA=operate(LintA)
            LstrA = [str(x) for x in LintA]
            A = int( ''.join(LstrA) )


    
