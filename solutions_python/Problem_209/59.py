PI = 3.14159265359


def calc_area(rm, RH):
    return PI*(rm*rm + 2*sum(RH))


def solve(N, K, R, H):
    ans = -1
    for i in range(N):
        R1 = R[:i] + R[i+1:]
        H1 = H[:i] + H[i+1:]
        RH1 = sorted([R1[j]*H1[j] for j in range(len(R1))], reverse=True)[:K-1]
        RH1 += [R[i]*H[i]]
        area = calc_area(R[i], RH1)
        ans = max(area, ans)
    return ans


def main():
    # f_in = open('A-small-test.in')
    # f_in = open('A-small-attempt0.in')
    f_in = open('A-large.in')
    # f_out = open('A-small.out', 'w')
    f_out = open('A-large.out', 'w')
    T = int(f_in.readline())
    for t in range(T):
        N, K = [int(i) for i in f_in.readline().split()]
        R = []
        H = []
        for _ in range(N):
            r, h = [int(i) for i in f_in.readline().split()]
            R.append(r)
            H.append(h)
        s = solve(N, K, R, H)
        f_out.write("Case #{}: {:.7f}\n".format(t+1, s))
        print "Case #{}: {:.7f}\n".format(t+1, s),
    f_in.close()
    f_out.close()

if __name__ == '__main__':
    main()
