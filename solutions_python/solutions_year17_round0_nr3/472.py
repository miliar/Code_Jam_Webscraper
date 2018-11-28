def lr(N):
    minx = (N-1) // 2
    maxx = (minx + 1) if (N-1) % 2 == 1 else minx
    return str(maxx) + " " + str(minx)

def evalAns(N, K):
    # if K == 1: return lr(N)
    p2 = 1
    while K >= p2: p2 <<= 1
    p2 >>= 1
    a = (N - p2 + 1) // p2
    b = (N - p2 + 1) % p2
    K -= p2 - 1
    if (K > b): return lr(a)
    else: return lr(a+1)

def main():
    # read the input file
    f = open("C-large.in", "r")
    s = f.read().split("\n")
    f.close()
    
    T = eval(s.pop(0))
    outputsStr = ""
    for i in range(T):
        N, K = [eval(k) for k in s.pop(0).split()]
        res = evalAns(N, K)
        outputsStr += "Case #%d: %s%s" % (i+1, str(res), "\n" if i < T-1 else "")
    
    f = open("c-large.out", "w")
    f.write(outputsStr)
    f.close()

main()
