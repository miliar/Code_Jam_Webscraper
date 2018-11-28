inputFile = 'C-large.in'

with open(inputFile, 'r') as f:
    rawInput = f.readlines()

numTestCases = int(rawInput[0].strip())

for caseNum in range(1, numTestCases+1):
    parts = rawInput[caseNum].split()
    
    N = int(parts[0])
    K = int(parts[1])
    
    tempK = K
    power = 0
    while (tempK > 1):
        tempK //= 2
        power += 1
        
    numRepeats = power + 1
    minRepeat = 2 ** numRepeats
    
    minLsRs = (N - K) // minRepeat
    maxLsRs = (N - K + (minRepeat // 2)) // minRepeat
    
    print('Case #{}: {} {}'.format(caseNum, maxLsRs, minLsRs))
        