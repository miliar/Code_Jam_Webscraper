def solve(N, P, G):
    print N, P, G
    G1 = [i % P for i in G]
    print G1
    d = [0, 0, 0, 0]
    for i in G1:
        d[i] += 1
    print d
    if P == 2:
        return d[0] + (d[1]+1)/2
    if P == 3:
        return d[0] + min(d[1], d[2]) + (abs(d[1]-d[2])+2)/3
    if P == 4:
        ans = d[0]
        t = min(d[3], d[1])
        ans += t
        d[3] -= t
        d[1] -= t
        t = d[2]/2
        ans += t
        d[2] -= 2*t
        if d[2]:
            ans += 1
            d[3] -= 2
            d[1] -= 2
        ans += (max(d[1], d[3])+3)/4
        return ans


def main():
    # f_in = open('A-small-test.in')
    # f_in = open('A-small-attempt0.in')
    f_in = open('A-large.in')
    # f_out = open('A-small.out', 'w')
    f_out = open('A-large.out', 'w')
    T = int(f_in.readline())
    for t in range(T):
        N, P = [int(i) for i in f_in.readline().split()]
        G = [int(i) for i in f_in.readline().split()]
        s = solve(N, P, G)
        f_out.write("Case #{}: {}\n".format(t+1, s))
        print "Case #{}: {}\n".format(t+1, s),
    f_in.close()
    f_out.close()

if __name__ == '__main__':
    main()
