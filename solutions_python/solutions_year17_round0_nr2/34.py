T = int(input())
for t in range(1,T+1):
    V, A = [0]+[int(_) for _ in input()], [0]
    while len(A) < len(V): A.append(max(d for d in range(A[-1],10) if A+[d]*(len(V)-len(A)) <= V))
    print('Case #{}: {}'.format(t,int(''.join(str(_) for _ in A[1:]))))
