
def solve(K,ind):
    nextd = "1234567890"
    prevd = "9012345678"

    if ind >= len(K):
        return "".join(K)

    if ind < 0:
        K = K[1:]
        return solve(K,ind+1)

    if ind == 0 and K[0] == '0':
        K = K[1:]
        K = ['9' for i in K]
        return solve(K,0)

    if ind > 0:
        if not K[ind] >= K[ind-1]:
            return solve(K,ind-1)

    if ind < len(K)-1:
        if not K[ind] <= K[ind+1]:
            K[ind] = prevd[int(K[ind])]
            K[ind+1:] = ['9' for i in range(len(K[ind+1:]))]
            return solve(K,ind)

    return solve(K,ind+1)



f = open("B-large.in","r")
g = open("output.txt","w")

T = int(f.readline())

for i in range(1,T+1):
    K=[i for i in f.readline().strip()]

    # Solve
    ans = solve(K,0)

    g.write("Case #{}: {}\n".format(i,ans))

f.close()
g.close()
