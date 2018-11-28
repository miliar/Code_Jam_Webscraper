inputFile = 'B-large.in'

with open(inputFile, 'r') as f:
    rawInput = f.readlines()

numTestCases = int(rawInput[0].strip())

def is_tidy(num):
    if num < 10:
        return True, -1

    strNum = str(num)
    for i, c in enumerate(strNum):
        if i == 0:
            continue
        if int(c) < int(strNum[i-1]):
            return False, len(strNum) - i
    
    return True, -1

for caseNum in range(1, numTestCases+1):
    N = int(rawInput[caseNum])
    
    printed = False
    
    isNTidy, pos = is_tidy(N)
    while (isNTidy == False):
        N = N - 10**pos 
        
        # Two cases, N = 0 or N != 0
        if (N == 0):
            print('Case #{}: {}'.format(caseNum, 10**pos - 1)) 
            printed = True
            break
        else:
            tempStr = ''
            for i in range(pos):
                tempStr += '9'
            N = int(str(N)[0:-pos] + tempStr)
        
        # Next loop
        isNTidy, pos = is_tidy(N)
    
    if printed:
        continue
    
    if (isNTidy == True):
        print('Case #{}: {}'.format(caseNum, N))
    