#A

import sys

infile = open(sys.argv[1])
outfile = open("A-attempt.out", 'w')
T = int(infile.readline())

for caseNum in range(1, T+1):
    K, S = infile.readline().split()
    numToAdd = 0
    numStanding = 0
    for k in range(int(K)+1):
        if (int(S[k]) > 0 and k > numStanding):
            numToAdd += k - numStanding
            numStanding += numToAdd
        numStanding += int(S[k]) 
            
        print(k, numStanding)    
    print("Case #%d: %d" % (caseNum, numToAdd), file=outfile)
