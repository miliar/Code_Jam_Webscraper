def solve(N, K):
    ans = -1
    d = [[1, (N-1)/2, N/2, 0, (N-1)/2, (N-1)/2]]
    while not (d[-1][1] == 0 and d[-1][2] == 0):
        k1, n1, n2, k2, n3, n4 = d[-1]
        nr1 = min(n1, n2, n3, n4)
        nr2 = nr1 + 1
        kr1 = k1*(n1 == nr1) + k1*(n2 == nr1) + k2*(n3 == nr1) + k2*(n4 == nr1)
        kr2 = 2*(k1+k2) - kr1
        d.append([kr2, (nr2-1)/2, nr2/2, kr1, (nr1-1)/2, nr1/2])
    k = 0
    for dd in d:
        k += dd[0]
        ans = [dd[2], dd[1]]
        if k >= K:
            break
        k += dd[3]
        ans = [dd[5], dd[4]]
        if k >= K:
            break
    return ' '.join(str(i) for i in ans)


def main():
    # f_in = open('C-small-test.in')
    # f_in = open('C-small-2-attempt0.in')
    f_in = open('C-large.in')
    # f_out = open('C-small.out', 'w')
    f_out = open('C-large.out', 'w')
    T = int(f_in.readline())
    for t in range(T):
        N, K = [int(i) for i in f_in.readline().split()]
        s = solve(N, K)
        f_out.write("Case #{}: {}\n".format(t+1, s))
        print "Case #{}: {}\n".format(t+1, s),
    f_in.close()
    f_out.close()

if __name__ == '__main__':
    main()
