T = input()
for caseID in range(1,T+1):
    inpTokens = raw_input().split()
    N = int(inpTokens[0])
    elapsed = 0
    lastB = [1,0]
    lastO = [1,0]
    for i in range(1,N+1):
        pos = int(inpTokens[i*2])
        if inpTokens[i*2-1] == 'O':
            nxtTime = lastO[1] + abs(pos - lastO[0])
            if nxtTime > elapsed:
                elapsed = nxtTime + 1
            else:
                elapsed = elapsed + 1
            lastO = [pos,elapsed]
        else:
            nxtTime = lastB[1] + abs(pos - lastB[0])
            if nxtTime > elapsed:
                elapsed = nxtTime + 1
            else:
                elapsed = elapsed + 1
            lastB = [pos,elapsed]
    print "Case #%d: %d" % (caseID,elapsed)
