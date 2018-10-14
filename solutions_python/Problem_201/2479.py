
fin = open('stalls.in','r')
fout = open('stalls.out','w')

T = int(fin.readline())
for t0 in range(T):
    N, K = map(int, fin.readline().split())
    
    stalls = [0 for i in range(N+2)]
    stalls[0] = 1
    stalls[N+1] = 1

    recordmaxlsrs = float('-inf')
    recordminlsrs = float('-inf')
    for i in range(K):
        left = [0 for _ in range(N+2)]
        right = [0 for _ in range(N+2)]
        lastleft = 0
        lastright = 0
        for j in range(N+2):
            if stalls[j] == 1 or (j > 0 and stalls[j - 1] == 1):
                lastleft = 0
            else:
                lastleft += 1
            left[j] = lastleft
            if stalls[N + 2 - j - 1] == 1 or (j > 0 and stalls[N + 2 - j]):
                lastright = 0
            else:
                lastright += 1
            right[N - j + 1] = lastright

        best = 0
        minlsrs = float('-inf')
        maxlsrs = float('-inf')
        
        for j in range(N):
            minlr = min(left[j], right[j])
            if minlr > minlsrs or (minlr == minlsrs and max(left[j], right[j]) > maxlsrs):
                best = j
                minlsrs = minlr
                maxlsrs = max(left[j], right[j])

        recordmaxlsrs = maxlsrs
        recordminlsrs = minlsrs
        stalls[best] = 1
        #print 'L', left
        #print 'R', right
        #print stalls
    
    fout.write("Case #" + str(t0 + 1) + ": " + str(recordmaxlsrs) + " " + str(recordminlsrs) + "\n")
