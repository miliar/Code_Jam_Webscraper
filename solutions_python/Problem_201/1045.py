
if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N,K = (int(i) for i in input().split())
        N = [N]
        for k in range(K):
            n = N.pop(0)
            nn = int(n/2)
            y,z = (nn-0, n-(nn+1))
            if k == K-1:
                print("Case #%d: %d %d" % (t+1, y, z) )
                break
            N += [y,z]
            N.sort(reverse=True)
