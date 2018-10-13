import string

# informations is a tuple (x_i, E_i, S_i)
# which gives the location, the range, and the speed of the town/horse in each spot
def solve(N, X, E, S):
    d = {}

    d[0] = 0
    for i in range(1, N):
        best = None
        times = [d[j] + (X[i] - X[j]) / S[j] if X[i] - X[j] <= E[j] else None for j in range(i)]
        valid = [v for v in times if v is not None]
        d[i] = min(valid)
    return d[N-1]


def test(inputs, ans):
    b = solve(*inputs)
    if (b != ans):
        print "Failed test! Inputs {} should give answer of {} not {}".format(' '.join(inputs), ans, b)

def main():

    outfile = open('a.out','w')
    T = int(string.strip(raw_input()))

    for k in xrange(1,T+1):
        print "Solving", k
        N, Q = map(int, string.strip(raw_input()).split())
        print "N, Q", N, Q
        # parse the lines here
        E = []
        S = []
        for j in range(N):
            E_i, S_i = map(float, string.strip(raw_input()).split())
            E.append(E_i)
            S.append(S_i)
        X = []
        x = 0
        for j in range(N):
            X.append(x)
            D = map(int, string.strip(raw_input()).split())
            D = [d for d in D if d != -1]
            if sum(D) > 0:
                x += float(sum(D))

        # throw away U, V
        _ = raw_input()

        answer = solve(N, X, E, S)

        outfile.write('Case #%d: %s\n' % (k,answer))

if __name__ == '__main__':
    main()
