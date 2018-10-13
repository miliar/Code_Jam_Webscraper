from collections import deque
from time import time

def recycledNumbers(inFilename, outFilename, writeToFile=0):
    """GCJ2012 - Qualification: C. RecycledNumbers"""
    # Read input file
    if writeToFile:
        outFile = open(outFilename, 'w')
    with open(inFilename) as inFile:
        # Read number of test cases T
        T = int(inFile.readline())
        print("T = " + str(T))
        
        # For each test case t:
        for t in range(T):
            # Read A and B; store number of digits
            A, B = [int(x) for x in inFile.readline().split()]
            numDigits = len(str(A))
            print("\n#{t}: A = {A}, B = {B}, #digits = {numDigits}".format(t=t+1, A=A, B=B, numDigits=numDigits))
            
            # Loop for n = A to B, count possible recycled pairs
            count = 0
            ctr = 0 # count the number of operations performed
            startTime = time()
            if(numDigits > 1):
                for n in range(A, B + 1):
                    nstr = str(n)
                    #print("n =", nstr)
                    
                    # Find length of longest repeating subsequence
                    bestSeq = ""
                    bestSeqLen = 0
                    for seqLen in range(1, int(numDigits / 2 + 1)):
                        nseq = nstr[:seqLen]
                        isGood = True
                        for nextSeqPos in range(seqLen, numDigits, seqLen):
                            nextSeq = nstr[nextSeqPos:(nextSeqPos+seqLen)]
                            if(nseq != nextSeq):
                                isGood = False
                                break

                        if(isGood):
                            bestSeq = nseq
                            bestSeqLen = seqLen

                    if bestSeqLen == 0:
                        bestSeq = nstr
                        bestSeqLen = numDigits

                    #print("Good: ", bestSeq, "\tLen: ", bestSeqLen)
                    #input("Press ENTER to continue...")

                    if bestSeqLen > 1:
                        
                        # Deque rotation - slow!
                        #nq = deque(nstr)
                        #mq = nq # in case we need nq later
                        #print(mq)

                        # String slicing - faster
                        mstr = nstr
                        
                        for digit in range(1, bestSeqLen):
                            ctr = ctr + 1

                            # Deque rotation - slow!
                            #mq.rotate(1)
                            #mstr = [''.join(mq)][0]

                            # String slicing - faster
                            mstr = mstr[numDigits-1:] + mstr[:numDigits-1]
                            #print(nstr, mstr)

                            m = int(mstr)
                            if n < m and (A <= m and m <= B):
                                count = count + 1
                                #print(count, n, m, sep='\t')

            elapsedTime = time() - startTime
            
            finalCount = count #int(count / 2) # all pairs are double counted
            outStr = "Case #{t}: {c}".format(t=t+1,c=finalCount)
            if writeToFile:
                print(outStr, file=outFile)
            print(outStr)
            print("#rotates:", ctr, ", time:", elapsedTime)

            #if t > 1:
            #    return

# Run on input
#recycledNumbers("C-sample.in", "C-sample.out")
#recycledNumbers("C-sample-mod.in", "C-sample-mod.out")
#recycledNumbers("C-small-attempt0.in", "C-small-attempt0.out")
recycledNumbers("C-large.in", "C-large.out", 1)
