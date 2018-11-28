
T = int(raw_input())

for cs in range(1, T + 1):
    B = raw_input().split(' ')
    A = int(B[0])
    B = int(B[1])

    woohah = set()

    for brute in range(A, B + 1):
        strin = str(brute)

        for aa in range(1, len(strin)):
            generator = strin[aa:] + strin[:aa]

            # zero character at index 0
            if generator[0] == '0': continue

            # out of bound
            if int(generator) > B or int(generator) < A: continue

            # same game
            if int(generator) == brute: continue

            pair = (int(generator), brute)

            if brute < int(generator):
                pair = (brute, int(generator))

            woohah.add(pair)

    print 'Case #%d: %d' % (cs, len(woohah))
