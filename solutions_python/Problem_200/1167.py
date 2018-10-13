T = input()
for t in range(T):
    N = input()
    '''
    N = map(int, list(raw_input()))

    smallified=False
    for i in range(len(N)):
        if smallified:
            N[i] = 9
            continue

        if i!=len(N)-1:
            if N[i]>N[i+1]:
                N[i] = N[i]-1
                smallified = True
    N = ''.join(map(str, N))
    '''

    tested = False
    while not tested:
        N1 = list(str(N))
        N2 = sorted(N1)

        if ''.join(N1)==''.join(N2):
            tested = True
        else:
            N -= 1

    print "Case #%d: %d"%(t+1, int(N))
