def eta(Ki, Si, D):
    return (D-Ki)/float(Si)

def solve(D, N, Ks, Ss):
    etas = [eta(Ki, Si, D) for (Ki, Si) in zip(Ks, Ss)]
    max_eta = max(etas)
    return D/max_eta

def main():
    T = input()
    for i in range(T):
        D, N = map(int, raw_input().split())
        Ks, Ss = [], []
        for j in range(N):
            K, S = map(int, raw_input().split())
            Ks.append(K)
            Ss.append(S)
        print 'Case #%d: %.6f' % (i+1, solve(D, N, Ks, Ss))

main()
