from math import pi
from decimal import *
getcontext().prec = 12
def solve(N, K, C):
    D = list(map(lambda x: (x[0] * x[1],x[0]), C))
    
    E = []
    for i in range(N):
        E.append(D[i][1])
        
    R = []    
    D.sort(reverse = True)
    for i in range(N):
        R.append(D[i][1])
 
    s = 0
    for i in range(K-1):
        s += D[i][0]
    xemxet = R[:K-1]
    area = 0
    mx = 0
    
    for i in range(N):
        index = R.index(E[i])
        if index <= K -1:
            area = s + D[K-1][0]
            radius = xemxet + [D[K-1][1]]
        else:
            area = s+  D[index][0]
            radius = xemxet + [D[index][1]]

        
        radius.sort(reverse = True)
            
        mx = max(mx, Decimal((radius[0] ** 2 + 2 * area) * 3141592653589793))
    mx = str(mx)
    return mx[:-15] + '.' + mx[-15:]


with open("in","r") as reader, open("out",'w') as writer:
    t = int(reader.readline())
    for i in range(t):
        C = []
        N, K = map(int, reader.readline().split())
        for j in range(N):
            R,H = map(int, reader.readline().split())
            C.append((R,H))
        writer.write("Case #{}: {}\n".format(i+1, solve(N, K, C)))
