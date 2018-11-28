
def solve(D, N, Ks, Ss):
    h = 0

    Hs = [0] * N
    for i in range(N):
        tmp = (D - Ks[i]) / Ss[i]
        h = max(h, tmp)

    return D/h


tmp = input()

T = int(tmp)
#print(T)

for i in range(T):
    tmp2 = input().split()

    D = int(tmp2[0])
    N = int(tmp2[1])

    Ks = [0] * N
    Ss = [0] * N

    for j in range(N):
        tmp3 = input().split()
        Ks[j] = int(tmp3[0])
        Ss[j] = int(tmp3[1])

    h = solve(D, N, Ks, Ss)
    h_str = '%.6f'%h
    print("Case #" + str(i+1) + ": " + h_str)

# print(Ks)
# print(Ss)
#	print(tmp2)

