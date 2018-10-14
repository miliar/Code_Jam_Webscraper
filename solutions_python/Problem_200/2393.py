T = int(raw_input(""))

for o in range(1, T+1):
    N = int(raw_input(""))

    while True:
        S = [int(x) for x in list(str(N))]
        if sum([1 if S[i] > S[i+1] else 0 for i in range(len(S)-1)]) > 0:
            N -= 1
        else:
            break

    print "Case #%d: %d" % (o, N)
