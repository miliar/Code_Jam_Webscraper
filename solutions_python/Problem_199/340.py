def solve(ip, k):
    res  = 0
    imp = "IMPOSSIBLE"
    if sum(ip) == 0:
        return 0

    L = len(ip)

    for i in range(L):
        if ip[i]==1:
            if L-i < k :
                return imp
            for j in range(k):
                ip[i+j] ^= 1
            res += 1

    return res


if __name__ == "__main__":
    tc = int(input())
    for ti in range(tc):
        ip_,k_ = input().strip().split()
        k = int(k_)
        ip=[ 1 if c=="-" else 0 for c in ip_.strip()]
        print("Case #{0}: {1}".format(ti + 1, solve(ip,k)))
