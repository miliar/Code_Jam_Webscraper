def lct_minus(s):  # locate the first '-'
    for i in range(len(s)):
        if s[i] == '-':
            return i
    return -1

def flip(S, K):
    L = len(S)
    j = lct_minus(S)
    c = 0
    while j != -1:
        if j+K > L:
            return 'IMPOSSIBLE'
        for i in range(j, j+K):
            if S[i]=='+':
                S[i]='-'
            else:
                S[i]='+'
        j = lct_minus(S)
        c += 1
    return str(c)
        
        
        
"""
def flip(S, K):  # flips the pancakes until all == " + "
    L = len(S)
    j = lct_minus(S)
    if j == -1:
        return 0
    if j+K > L:
        return -50
    for i in range(j, j+K):
        if S[i]=='+':
            S[i]='-'
        else:
            S[i]='+'
    
    return 1 + flip(S, K)
"""       
I = "IMPOSSIBLE"

file = open('pan.txt')
ANS = open('ans.txt','w')

T = int(file.readline())
for i in range(T):
    S, K = [i for i in file.readline().split(' ')]
    S = list(S)
    K = int(K)
    ans = flip(S, K)
    a = str('Case #%d: %s\n'%(i+1,str(ans)))
    ANS.write(str(a))

"""
T = int(input())
for i in range(T):
    S, K = [i for i in input().split(' ')]
    S = list(S)
    K = int(K)
    ans = flip(S, K)
    if ans < 0 :
        print(I)
    else :
        print(ans)
"""
    
        
