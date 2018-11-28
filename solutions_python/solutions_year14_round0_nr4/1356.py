'''
Created on 13/04/2014
'''


import bisect

def processCase(t, N, Nblocks, Kblocks):

    Nblocks.sort()
    Kblocks.sort()
    
    Nblocks_ = Nblocks.copy()
    Kblocks_ = Kblocks.copy()

    # War game
    # --------
    z = 0
    for i in range(N):
        # Naomi strategy
        chosenN = Nblocks.pop(N - i - 1)
        toldN = chosenN
        
        # Ken strategy
        j = bisect.bisect_left(Kblocks, toldN)
        if (j >= N - i):    # Ken does not have a suitable block
            Kblocks.pop(0)
            z = z + 1
        else:               # Ken has a suitable block
            Kblocks.pop(j)


    Nblocks = Nblocks_
    Kblocks = Kblocks_
    # Deceitful War game
    # ------------------
    y = 0
    for i in range(N):
        # Naomi strategy
        maxN = Nblocks[N - i - 1]
        maxK = Kblocks[N - i - 1]
        
        minN = Nblocks[0]
        minK = Kblocks[0]
        
        if minN > minK:
            chosenN = Nblocks.pop(0)
            toldN = 1;      # Should be minK + epsilon, but bisect_left works
        else:
            chosenN = Nblocks.pop(0)
            toldN = maxK    # Should be maxK - epsilon, but bisect_left works

        # Ken strategy (unchanged)
        j = bisect.bisect_left(Kblocks, toldN)
        if (j >= N - i):    # Ken does not have a suitable block
            Kblocks.pop(0)
            y = y + 1
        else:               # Ken has a suitable block
            Kblocks.pop(j)

        

    print('Case #' + str(t+1) + ': ' + str(y) + ' ' + str(z))
    return 'Case #' + str(t+1) + ': ' + str(y) + ' ' + str(z) + '\n'


if __name__ == '__main__':
    myinput = open('D-large.in', 'r')
    myoutput = open('D-large.out', 'w')
    
    T = int(myinput.readline())
    
    for t in range(T):
        N = int(myinput.readline())
        Nblocks = list(map(float, myinput.readline().split()))
        Kblocks = list(map(float, myinput.readline().split()))
        myoutput.write(processCase(t, N, Nblocks, Kblocks))
    
    myoutput.close()
    myinput.close()