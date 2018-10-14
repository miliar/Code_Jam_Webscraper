with open('input.txt') as inp:
    with open('output.txt', 'w') as outp:
        ncases = int(inp.readline().strip())
        for nc in range(0, ncases):
            worst = 0
            D, N = inp.readline().strip().split(' ')
            for i in xrange(0, int(N)):
                K, S = inp.readline().strip().split(' ')
                travel = (float(D) - float(K)) / float(S)
                if travel > worst:
                    worst = travel
            outp.write("Case #{}: {}\n".format(nc + 1, float(D) / worst))
