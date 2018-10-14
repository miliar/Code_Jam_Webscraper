def flip(S, K, i):
    for j in range(i, i+K):
        if S[j] == '-':
            S[j] = '+'
        else:
            S[j] = '-'

with open("input.in", 'r') as f:
    with open("output.out", 'w') as g:
        T = int(f.readline())
        for r in range(T):
            S, K = f.readline().strip().split()
            K = int(K)
            S = list(S)
            flips = 0
            for i, x in enumerate(S):
                if i == len(S) - K + 1:
                    break
                if x == '+':
                    continue
                flip(S, K, i)
                flips += 1
            if all([x == '+' for x in S]):
                g.write("Case #%d: %d\n" % (r+1, flips))
            else:
                g.write("Case #%d: IMPOSSIBLE\n" % (r+1))
