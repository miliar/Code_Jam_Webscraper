import sys

with open(sys.argv[1], 'r') as inputFile, open('A-large.out', 'w') as outputFile:
    numTests = inputFile.readline()
    numTests = int(numTests.strip("\n"))
    for i in range(numTests):
        s, k = inputFile.readline().strip("\n").split()
        k = int(k)
        binarySwitchArray = [0 for i in range(len(s))]
        m = 0
        numFlips = 0
        while(m + k <= len(s)):
            if((binarySwitchArray[m] % 2 == 1 and s[m] == '+') or 
                (binarySwitchArray[m] % 2 == 0 and s[m] == '-')):
                    for num in range(m, m+k):
                        binarySwitchArray[num] += 1
                    numFlips += 1
            m += 1
        while(m < len(s)):
            if((binarySwitchArray[m] % 2 == 1 and s[m] == '+') or 
                (binarySwitchArray[m] % 2 == 0 and s[m] == '-')):
                    numFlips = "IMPOSSIBLE"
                    break
            m+=1
        outputFile.write("Case #{}: {}\n".format(i+1, numFlips))
    
