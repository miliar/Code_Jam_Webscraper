'''
Created on 7 abr. 2017

@author: Dennys
'''
from math import trunc

tree = []

def flip(S, K, pos):
    S1 = ''
    if pos + K <= len(S):
        for i in S[pos:pos + K]:
            S1 += '+' if i == '-' else '-'
        S1 = S[0:pos] + S1 + S[pos + K:]
    else:
        S1 = S
    return S1    

def validate(S):
    for i in S[:]:
        if i == '-':            
            return False
    return True

def reduce(S, K, pos):
    r = [S, 0, -1]        
    r[1] = S.count('-' * K)
    r[0] = S.replace('-' * K, '')    
    r[2] = pos - S[:pos].count('-' * K) * K        
    return r

def sol(SO, S, K, pos=0, n=float(0.0)):      
    if validate(S):        
        tree.append(n)
    else:
        r = reduce(S, K, pos)
        S = r[0]
        n += r[1]
        pos = r[2]
        if validate(S):        
            tree.append(n)
        else:
            if len(S) - K + 1 >= pos:            
                for i in range(pos, len(S) - K + 1):
                    S1 = flip(S, K, i)
                    sol(SO, S1, K, i + 1, n + 1)

if __name__ == '__main__':
    t = int(input())  # read a line with a single integer
    if t >= 1 and t <= 100: 
        for i in range(1, t + 1):
            S, K = [s for s in input().split(" ")]
            K = int(K)
            if len(S) >= 2 and len(S) <= 1000:
                if K >= 2 and K <= len(S):
                    ok = True
                    for j in S:
                        if j not in ['+', '-']:
                            ok = False
                            break
                    if ok:
                        tree = []
                        sol(S, S, K)
                        if len(tree) == 0:
                            print("Case #{}: {}".format(i, "IMPOSSIBLE"))
                        else:
                            m = 2 ** (len(S) - K + 1)
                            for x in tree:
                                if m > float(x):
                                    m = float(x)                             
                            print("Case #{}: {}".format(i, trunc(m)))
