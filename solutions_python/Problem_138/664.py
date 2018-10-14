def war(naomi, ken, N):
    naomi.sort()
    ken.sort()    
    fwar=0
    i=0
    for valn in naomi:
        while i<N and valn>ken[i]:
            i+=1
        else:
            if i<N:
                fwar+=1
                i+=1
            else:
                return N-fwar
        
    return N-fwar

def dwar(naomi, ken, N):
    naomi.sort()
    ken.sort()    
    dwar=0
    i=0
    for valk in ken:
        while i<N and valk>naomi[i]:
            i+=1
        else:
            if i<N:
                dwar+=1
                i+=1
            else:
                return dwar
        
    return dwar

t=int(input())
for i in range(t):
    N=int(input())
    naomi=list(map(float, input().split()))
    ken=list(map(float, input().split()))
    ans1=dwar(naomi, ken, N)
    ans2=war(naomi, ken, N)   
    print('Case #{0}: {1} {2}'.format(i+1, ans1, ans2))