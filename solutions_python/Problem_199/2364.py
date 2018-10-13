def flip(c):
    if c == '-':
        return '+'
    elif c == '+':
        return '-'
    else:
        raise Exception('Cannot flip [{}], not + or -.'.format(c))

def flips(s):
    out = ''
    for c in s:
        out += flip(c)
    return out
    
def doit(S,K,out):
    for i in range(len(S)):
        if S[i] == '-':
            if K+i > len(S):
                return 'IMPOSSIBLE'
            out += 1
            #print(out)
            A = S[:i]
            B = flips(S[i:K+i])
            C = S[K+i:]
            S = A+B+C
            #print('[{}][{}][{}]'.format(A,B,C))
            #print(S)
    return out

t = int(input())
for i in range(1, t+1):
    [S,K] = input().split(' ')
    K = int(K)
    #print(S)
    #print(K)
    out = doit(S,K,0)
    print('Case #{}: {}'.format(i, out))

