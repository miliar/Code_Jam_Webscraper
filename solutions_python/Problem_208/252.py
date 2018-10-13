def solve(N, Q, E, S, D, U, V):
    dist = []
    for i in range(N-1):
        dist.append(D[i][i+1])
    print dist
    print S
    print E

    s = [[dist[0]*1.0/S[0], S[0], E[0]-dist[0]]]
    print s

    for i in range(1, N-1):
        st = []
        mint = s[0][0]
        for j in range(len(s)):
            mint = min(mint, s[j][0])
            if S[i] < s[j][1] or E[i] < s[j][2]:
                if s[j][2] >= dist[i]:
                    st.append([s[j][0] + dist[i]/s[j][1], s[j][1], s[j][2]-dist[i]])
        if E[i] >= dist[i]:
            st.append([mint + dist[i]/S[i], S[i], E[i]-dist[i]])
        # print st
        s = st
    mint = s[0][0]
    for j in range(len(s)):
        mint = min(mint, s[j][0])
    return mint


def main():
    # f_in = open('C-small-test.in')
    f_in = open('C-small-attempt1.in')
    # f_in = open('C-large.in')
    f_out = open('C-small.out', 'w')
    # f_out = open('C-large.out', 'w')
    T = int(f_in.readline())
    for t in range(T):
        N, Q = [int(i) for i in f_in.readline().split()]
        E = []
        S = []
        for _ in range(N):
            e, s = [int(i) for i in f_in.readline().split()]
            E.append(e*1.0)
            S.append(s*1.0)
        D = []
        for _ in range(N):
            D.append([int(i)*1.0 for i in f_in.readline().split()])
        U = []
        V = []
        for _ in range(Q):
            u, v = [int(i) for i in f_in.readline().split()]
            U.append(e)
            V.append(s)
        s = solve(N, Q, E, S, D, U, V)
        f_out.write("Case #{}: {}\n".format(t+1, s))
        print "Case #{}: {}\n".format(t+1, s),
    f_in.close()
    f_out.close()

if __name__ == '__main__':
    main()
