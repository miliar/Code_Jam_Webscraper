import math

t = int(input())

for c in range(t):
    N,K = map(int,input().split())
    U = float(input())
    Cs = sorted(list(map(float,input().split())))
#     for i in range(N):
#         r,h = map(int,input().split())
#         pks.append((r,h))
    
    broke = False
    for i in range(2,N+1):
        c_up = Cs[:i]
        if i* max(c_up) - sum(c_up) > U:
            broke = True
            break
    if broke:
        i = i-1
        total = 1
        c_moy = (sum(Cs[:i])+U)/i
        total = c_moy**i
        for j in range(i,N):
            total *= Cs[j]
#         print(total)
#         totalFake = ((sum(Cs) + U)/len(Cs))**len(Cs)
#         print("broke",totalFake)
        print("Case #%s: %.10f"%(c+1,total))
    else:
        total = ((sum(Cs) + U)/len(Cs))**len(Cs)
        print("Case #%s: %.10f"%(c+1,total))
