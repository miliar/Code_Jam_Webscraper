def solve(N, K, U, P):
    ans = 1
    # print N, K, U, P
    for i in range(N):
        if P[i] != P[i+1]:
            inc = min(P[i+1] - P[i], U / (i+1))
            for j in range(i+1):
                P[j] += inc
            U -= inc * (i+1)
            if U == 0:
                break
    for i in range(N):
        ans *= P[i]
    return ans


def main():
    # f_in = open('C-small-test.in')
    f_in = open('C-small-1-attempt0.in')
    # f_in = open('C-large.in')
    f_out = open('C-small-1.out', 'w')
    # f_out = open('C-large.out', 'w')
    T = int(f_in.readline())
    for t in range(T):
        N, K = [int(i) for i in f_in.readline().split()]
        U = float(f_in.readline())
        P = sorted([float(i) for i in f_in.readline().split()])
        s = solve(N, K, U, P+[1.0])
        f_out.write("Case #{}: {:.6f}\n".format(t+1, s))
        print "Case #{}: {:.6f}\n".format(t+1, s),
    f_in.close()
    f_out.close()

if __name__ == '__main__':
    main()
