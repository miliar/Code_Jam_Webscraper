def not_tidy(N):
    for i in range(len(N)-1):
        if int(N[i]) > int(N[i+1]):
            return str(int(N[:i+1])-1) + '9'*(len(N)-i-1)
    return N


T = int(raw_input())

for i in range(T):
    N = raw_input()
    if len(N) == 1:
        print "Case #{0}: {1}".format(i+1, N)
        continue
    NN = not_tidy(N)
    while NN != N and len(NN) > 1:
        N = NN
        NN = not_tidy(N)
    print "Case #{0}: {1}".format(i+1, int(NN))
