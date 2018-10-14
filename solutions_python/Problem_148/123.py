import codejam as gcj

T = gcj.read_input('i')
for t in range(T):
    N, X, S = gcj.read_input('i i', 'i[<]')
    discs, i, j = 0, 0, N - 1

    while i <= j:
        if S[i] + S[j] <= X:
            i += 1

        j -= 1
        discs += 1

    print 'Case #%i:' % (t + 1), discs