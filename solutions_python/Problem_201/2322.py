import math

with open("C-small-2-attempt0.in") as fr:
    T = int(fr.readline())
    Ns = []
    Ks = []
    for i in range(T):
        line = fr.readline().split()
        Ns.append(line[0]) # can't use int since the large case up to 10**18 =~ 2**60
        Ks.append(line[1])
def solutionC_small(N, K):
    N=int(N)
    K=int(K)
    while K > 0:
        y, z = math.ceil((N-1)/2), math.floor((N-1)/2) # y=max(Ls, Rs) z=min(Ls, Rs)
        if K%2==0: # right side
            N = y
        else :
            N = z
        K = K//2
    return y, z


def solutionB_large(N):
    return N

with open('ans.txt', 'w', encoding='utf8') as fw:
    for index, (n, k) in enumerate(zip(Ns, Ks), start=1):
        y, z = solutionC_small(n, k)
        ans = "Case #{}: {} {}\n".format(index,y, z)
        fw.write(ans)