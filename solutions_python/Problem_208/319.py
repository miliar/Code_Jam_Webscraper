#input = list(open('in.txt'))[::-1].pop

def solve():
    N, Q = map(int, input().split())
    E, S = [], []
    for i in range(N):
        Ei, Si = map(int, input().split())
        E.append(Ei)
        S.append(Si)
    D = []
    for _ in range(N):
        D.append(list(map(int, input().split())))
    times = []
    for _ in range(Q):
        U, V = map(int, input().split())
        T = [0] + [float('inf')] * (N - 1)
        for i in range(N-1):
            d = 0 #d[i][i+1]
            for j in range(i+1, N):
                d += D[j-1][j]
                if d > E[i]:
                    break
                T[j] = min(T[j], T[i] + d / S[i])
        #return T
        #print
        times.append(T[-1])
        continue
                    
        t = 0
        e = 0
        s = 0
        #for ee, ss in zip(E[:-1], S[:-1]):
        for i in range(N - 1):
            D = d[i][i+1]
            #if e < D or E[i] >= D 
                
        times.append(42)
    return ' '.join(map(str, times))

T = int(input())
for x in range(1, T+1):
    print('Case #{}: {}'.format(x, solve()))
